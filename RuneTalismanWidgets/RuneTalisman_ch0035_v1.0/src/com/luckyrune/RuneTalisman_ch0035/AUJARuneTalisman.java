package com.luckyrune.RuneTalisman_ch0035;

import android.app.PendingIntent;
import android.appwidget.AppWidgetManager;
import android.appwidget.AppWidgetProvider;
import android.content.Context;
import android.content.Intent;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.RemoteViews;

public class AUJARuneTalisman extends AppWidgetProvider implements
		View.OnClickListener {
	private static final String TAG = "AUJARuneTalisman";
	//private Button runeButton;

	public void onClick(View v) {
		Log.d(TAG, "onClick()");

	}

	public void onUpdate(Context context, AppWidgetManager appWidgetManager,
			int[] appWidgetIds) {
		final int N = appWidgetIds.length;
		Log.d(TAG, "onUpdate()");
		// Perform this loop procedure for each App Widget that belongs to this
		// provider
		for (int i = 0; i < N; i++) {
			int appWidgetId = appWidgetIds[i];

			// Create an Intent to launch ExampleActivity
			Intent intent = new Intent(context,
					com.luckyrune.RuneTalisman_ch0035.RuneInfo.class);
			PendingIntent pendingIntent = PendingIntent.getActivity(context, 0,
					intent, 0);
			Log.d(TAG, "onUpdate() Sending intent:" + pendingIntent.toString());
			// Get the layout for the App Widget and attach an on-click listener
			// to the button
			RemoteViews views = new RemoteViews(context.getPackageName(),
					R.layout.widget);
			views.setOnClickPendingIntent(R.id.image_view, pendingIntent);

			// Tell the AppWidgetManager to perform an update on the current App
			// Widget
			appWidgetManager.updateAppWidget(appWidgetId, views);
		}
	}

	@Override
	public void onDeleted(Context context, int[] appWidgetIds) {
		Log.d(TAG, "onDeleted()");

	}

	@Override
	public void onEnabled(Context context) {
		Log.d(TAG, "onEnabled()");
	}

	@Override
	public void onDisabled(Context context) {
		Log.d(TAG, "onDisabled()");
	}

	static void updateAppWidget(Context context,
			AppWidgetManager appWidgetManager, int appWidgetId,
			String titlePrefix) {
		Log.d(TAG, "updateAppWidget() appWidgetId=" + appWidgetId
				+ " titlePrefix=" + titlePrefix);
	}
}
