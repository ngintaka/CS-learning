package com.google.android.apps.memegen;

import java.util.List;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.AdapterView.OnItemClickListener;
import android.widget.GridView;

public class SelectMemeActivity extends Activity {
	private ImageAdapter adapter;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_select_meme);
		GridView gridView = (GridView) findViewById(R.id.gridview);
		adapter = new ImageAdapter(this);
		gridView.setAdapter(adapter);

		gridView.setOnItemClickListener(new OnItemClickListener() {
			@Override
			public void onItemClick(AdapterView<?> parent, View v,
					int position, long id) {
				Intent intent = new Intent(SelectMemeActivity.this,
						CreateMemeActivity.class);
				intent.putExtra("meme_url", (String) adapter.getItem(position));
				startActivity(intent);
			}
		});
	}

/*	@Override
	protected void onStart() {
		super.onStart();

		JsonParser atomParser = new JsonParser();
		atomParser.parse(new JsonParser.ParseCompleteCallback() {

			@Override
			public void onParseComplete(List<String> urls) {
				adapter.setImageUrls(urls);
				adapter.notifyDataSetChanged();
			}
		});

	}
*/
}