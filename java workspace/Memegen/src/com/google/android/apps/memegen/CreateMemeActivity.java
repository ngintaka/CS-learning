package com.google.android.apps.memegen;

import java.io.IOException;
import java.io.InputStream;
import java.net.URL;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.BitmapFactory;
import android.net.Uri;
import android.os.AsyncTask;
import android.os.Bundle;
import android.provider.MediaStore;
import android.text.Editable;
import android.text.TextWatcher;
import android.util.Log;
import android.view.Menu;
import android.view.MenuItem;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.RelativeLayout;
import android.widget.TextView;
import android.widget.Toast;

public class CreateMemeActivity extends Activity {
	private EditText topEditText;
	private TextView topText;
	private EditText bottomEditText;
	private TextView bottomText;
	private RelativeLayout meme;
	private ImageView memeTemplate;

	private final static class CopyTextWatcher implements TextWatcher {
		private final TextView textView;

		public CopyTextWatcher(TextView destination) {
			textView = destination;
		}

		@Override
		public void onTextChanged(CharSequence s, int start, int before,
				int count) {
		}

		@Override
		public void beforeTextChanged(CharSequence s, int start, int count,
				int after) {
		}

		@Override
		public void afterTextChanged(Editable s) {
			textView.setText(s.toString());
		}
	}

	class DownloadImageAsyncTask extends AsyncTask<String, Void, Bitmap> {

		@Override
		protected Bitmap doInBackground(String... arg0) {
			String imageUrl = arg0[0];
			try {
				return BitmapFactory.decodeStream((InputStream) new URL(
						imageUrl).getContent());

			} catch (IOException e) {
				Log.e("DownloadImageAsyncTask",
						"Error reading bitmap from URL: " + imageUrl, e);
			}
			return null;
		}

		@Override
		protected void onPostExecute(Bitmap result) {
			if (result != null) {
				memeTemplate.setImageBitmap(result);
			}
		}
	}

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_create_meme);

		topText = (TextView) findViewById(R.id.top_text);
		topEditText = (EditText) findViewById(R.id.top_text_edit);
		topEditText.addTextChangedListener(new CopyTextWatcher(topText));

		bottomText = (TextView) findViewById(R.id.bottom_text);
		bottomEditText = (EditText) findViewById(R.id.bottom_text_edit);
		bottomEditText.addTextChangedListener(new CopyTextWatcher(bottomText));

		meme = (RelativeLayout) findViewById(R.id.meme);

		memeTemplate = (ImageView) findViewById(R.id.meme_image);
	}

	@Override
	protected void onStart() {
		super.onStart();
		Intent intent = getIntent();
		if (intent != null) {
			String url = intent.getExtras().getString("meme_url");
			new DownloadImageAsyncTask().execute(url);
		}
	}

	private String save() {
		// force a refresh of the view drawing cache:
		meme.setDrawingCacheEnabled(false);
		meme.setDrawingCacheEnabled(true);

		Bitmap bitmap = Bitmap.createBitmap(meme.getDrawingCache());
		return MediaStore.Images.Media.insertImage(getContentResolver(),
				bitmap, "meme", "meme");
	}

	private void share() {
		String url = save();
		if (url != null) {
			Intent share = new Intent(Intent.ACTION_SEND);
			share.setType("image/jpg");
			share.putExtra(Intent.EXTRA_STREAM, Uri.parse(url));
			startActivity(Intent.createChooser(share,
					getString(R.string.share_tag)));
		} else {
			Toast.makeText(this, "Error sharing the meme!", Toast.LENGTH_LONG)
					.show();
		}
	}

	@Override
	public boolean onCreateOptionsMenu(Menu menu) {
		// Inflate the menu; this adds items to the action bar if it is present.
		getMenuInflater().inflate(R.menu.create_meme, menu);
		return true;
	}

	@Override
	public boolean onOptionsItemSelected(MenuItem item) {
		switch (item.getItemId()) {
		case R.id.share:
			share();
			return true;
		default:
			return super.onOptionsItemSelected(item);
		}
	}

}
