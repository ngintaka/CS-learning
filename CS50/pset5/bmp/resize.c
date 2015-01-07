/**
 * copy.c
 *
 * Computer Science 50
 * Problem Set 5
 *
 * Copies a BMP piece by piece, just because.
 */
       
#include <stdio.h>
#include <stdlib.h>

#include "bmp.h"

int main(int argc, char* argv[])
{
    // ensure proper usage
    if (argc != 4)
    {
        printf("Usage: ./copy infile outfile\n");
        return 1;
    }

    // remember filenames
    int scale = atoi(argv[1]);
    char* infile = argv[2];
    char* outfile = argv[3];
       
    //check scale is OK
    if (scale < 1 || scale > 100)
    {
        printf("Please provide an integer between 1 and 100");
        return 5;
    }

    // open input file 
    FILE* inptr = fopen(infile, "r");
    if (inptr == NULL)
    {
        printf("Could not open %s.\n", infile);
        return 2;
    }

    // open output file
    FILE* outptr = fopen(outfile, "w");
    if (outptr == NULL)
    {
        fclose(inptr);
        fprintf(stderr, "Could not create %s.\n", outfile);
        return 3;
    }

    // read infile's BITMAPFILEHEADER
    BITMAPFILEHEADER bf;
    fread(&bf, sizeof(BITMAPFILEHEADER), 1, inptr);

    // read infile's BITMAPINFOHEADER
    BITMAPINFOHEADER bi;
    fread(&bi, sizeof(BITMAPINFOHEADER), 1, inptr);

    // ensure infile is (likely) a 24-bit uncompressed BMP 4.0
    if (bf.bfType != 0x4d42 || bf.bfOffBits != 54 || bi.biSize != 40 || 
        bi.biBitCount != 24 || bi.biCompression != 0)
    {
        fclose(outptr);
        fclose(inptr);
        fprintf(stderr, "Unsupported file format.\n");
        return 4;
    }

    //record original size values
    //int orig_bfSize = bf.bfSize;
    int orig_biWidth = bi.biWidth;
    int orig_biHeight = bi.biHeight;
    
    //update header values due to scaling
    bi.biWidth = orig_biWidth * scale;
    bi.biHeight = orig_biHeight * scale;
    

    // determine padding for scanlines
    int orig_padding = (4 - (orig_biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    
    int new_padding =  (4 - (bi.biWidth * sizeof(RGBTRIPLE)) % 4) % 4;
    
    bf.bfSize = ((bi.biWidth*3 + new_padding) * abs(bi.biHeight)) + 54;
    bi.biSizeImage = bf.bfSize - 54;
    
    // write outfile's BITMAPFILEHEADER
    fwrite(&bf, sizeof(BITMAPFILEHEADER), 1, outptr);

    // write outfile's BITMAPINFOHEADER
    fwrite(&bi, sizeof(BITMAPINFOHEADER), 1, outptr);


    // iterate over infile's scanlines    
    int count = 1;
    for (int i = 0, biHeight = abs(bi.biHeight); i < biHeight; i++)
    {      
        
        // iterate over pixels in scanline             
        for (int j = 0; j < orig_biWidth; j++)
        {
            // temporary storage
            RGBTRIPLE triple;

            // read RGB triple from infile
            fread(&triple, sizeof(RGBTRIPLE), 1, inptr);

            // write RGB triple to outfile
            for (int k = 0; k < scale; k++) //copy horizontally
            {
                fwrite(&triple, sizeof(RGBTRIPLE), 1, outptr);
            }                                        
        }
        
        // add new padding
        for (int p = 0; p < new_padding; p++)
        {
            fputc(0x00, outptr);
        }     
        if (count % scale != 0)
        {
            // skip back to beginning of row
            fseek(inptr, -(orig_biWidth*3), SEEK_CUR);
        }
        else
        {
            // skip over padding, if any 
            fseek(inptr, orig_padding, SEEK_CUR);
        }
        count ++;
    }
  
    // close infile
    fclose(inptr);

    // close outfile
    fclose(outptr);

    // that's all folks
    return 0;
}
