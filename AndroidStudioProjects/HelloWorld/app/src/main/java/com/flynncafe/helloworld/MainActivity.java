package com.flynncafe.helloworld;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.view.Menu;
import android.view.MenuItem;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.EditText;
import android.widget.RelativeLayout;
import android.widget.TextView;


public class MainActivity extends Activity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

    Button button1 = (Button)findViewById(R.id.ok);
    button1.setOnClickListener(new OnClickListener(){
        public void onClick(View v) {
            Intent myIntent = new Intent(v.getContext(), NextActivity.class);
            startActivityForResult(myIntent, 0);
        }
    });

    Button button2 = (Button)findViewById(R.id.cancel);
    button2.setOnClickListener(new OnClickListener(){
        public void onClick(View v) {
            EditText text = (EditText)findViewById(R.id.editText2);
            text.setText(R.string.str5);
        }
    });
    }

    @Override
    public boolean onCreateOptionsMenu(Menu menu) {
        // Inflate the menu; this adds items to the action bar if it is present.
        getMenuInflater().inflate(R.menu.main, menu);
        return true;
    }

    @Override
    public boolean onOptionsItemSelected(MenuItem item) {
        // Handle action bar item clicks here. The action bar will
        // automatically handle clicks on the Home/Up button, so long
        // as you specify a parent activity in AndroidManifest.xml.
        RelativeLayout bkgr = (RelativeLayout)findViewById(R.id.back);
        EditText text = (EditText)findViewById(R.id.editText2);
        switch(item.getItemId()) {
            case R.id.action_settings1:
                text.setText("Settings selected");
                return true;

            case R.id.action_settings2:
                text.setText("Dog Breath selected");
                return true;
        }

        return super.onOptionsItemSelected(item);
    }
}