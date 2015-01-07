package com.google.android.apps.memegen;

import java.io.IOException;
import java.io.InputStream;
import java.net.URL;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Set;

import android.annotation.TargetApi;
import android.content.Context;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.os.AsyncTask;
import android.os.Build;
import android.util.Log;
import android.util.LruCache;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.GridView;
import android.widget.ImageView;

@TargetApi(Build.VERSION_CODES.HONEYCOMB_MR1)
public class ImageAdapter extends BaseAdapter {
	private final Context context;
	private List<String> imageUrls = new ArrayList<String>();

	private LruCache<String, Bitmap> imageCache = new LruCache<String, Bitmap>(
			1000);
	private final Set<String> downloadingImageUrls = new HashSet<String>();

	public void setImageUrls(List<String> imageUrls) {
		this.imageUrls = imageUrls;
	}

	ImageAdapter(Context c) {
		context = c;
	}

	@Override
	public int getCount() {
		return imageUrls.size();
	}

	@Override
	public Object getItem(int position) {
		if (position >= imageUrls.size()) {
			return null;
		}
		return imageUrls.get(position);
	}

	@Override
	public long getItemId(int arg0) {
		return 0;
	}

	@Override
	public View getView(int position, View convertView, ViewGroup parent) {

		ImageView imageView;
		if (convertView == null) {
			imageView = new ImageView(context);
			imageView.setLayoutParams(new GridView.LayoutParams(150, 150));
			imageView.setScaleType(ImageView.ScaleType.CENTER_CROP);
			imageView.setPadding(8, 8, 8, 8);
		} else {
			imageView = (ImageView) convertView;
			imageView.setImageDrawable(null);
		}

		if (position >= imageUrls.size()) {
			return imageView;
		}
		try {
			String imageUrl = imageUrls.get(position);
			Bitmap bitmap = imageCache.get(imageUrl);
			if (bitmap != null) {
				imageView.setImageBitmap(bitmap);
			} else {
				if (!downloadingImageUrls.contains(imageUrl)) {
					downloadingImageUrls.add(imageUrl);
					new DownloadImageAsyncTask(imageUrl).execute();		
				}
			}
		} catch (Exception e) {
			Log.e("ImageAdapter", "Error downloading image", e);
		}

		return imageView;
	}

	class DownloadImageAsyncTask extends AsyncTask<Void, Void, Void> {
		private final String imageUrl;

		public DownloadImageAsyncTask(String imageUrl) {
			this.imageUrl = imageUrl;
		}

		@Override
		protected void onPreExecute() {
			Log.i("DownloadImageAsyncTask", "Starting image download task...");
		}

		@Override
		protected Void doInBackground(Void... params) {
			try {
				Bitmap bitmap = BitmapFactory
						.decodeStream((InputStream) new URL(imageUrl)
								.getContent());
				imageCache.put(imageUrl, bitmap);
			} catch (IOException e) {
				Log.e("DownloadImageAsyncTask", "Error reading bitmap" + e);
			}
			return null;
		}

		@Override
		protected void onPostExecute(Void result) {
			downloadingImageUrls.remove(imageUrl);
			notifyDataSetChanged();
		}
	}

}
