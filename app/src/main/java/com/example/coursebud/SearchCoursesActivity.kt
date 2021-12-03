package com.example.coursebud

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.SearchView
import android.widget.TextView

class SearchCoursesActivity : AppCompatActivity() {

    private lateinit var courseBudText: TextView
    private lateinit var searchView: SearchView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.search_courses)

        courseBudText = findViewById(R.id.courseBudText)
        searchView = findViewById((R.id.searchView))
    }
}