package com.luckyrune.RuneTalisman_ch0025;

import android.app.Activity;
import android.content.Context;
import android.content.res.Resources;
import android.graphics.drawable.Drawable;
import android.graphics.drawable.ShapeDrawable;
import android.os.Bundle;
import android.text.Html;
import android.text.Spanned;
import android.text.Html.ImageGetter;
import android.util.Log;
import android.webkit.WebView;
import android.widget.TextView;

public class RuneInfo extends Activity {
	private static final String TAG = "RuneInfo";
	//private TextView mainTextView;
	private WebView mainTextView;
	protected Context myContext;
	
    /** Called when the activity is first created. */
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        myContext = this;
        setContentView(R.layout.main);
        //mainTextView = (TextView) findViewById(R.id.info_main_text_view);
        mainTextView = (WebView) findViewById(R.id.info_main_text_view);
        //mainTextView.loadData(RuneTalismanData.talisman_info, "text/html", "utf-8");
        mainTextView.getSettings().setJavaScriptEnabled(false);
        mainTextView.loadUrl("file:///android_asset/info.html");
     }
}