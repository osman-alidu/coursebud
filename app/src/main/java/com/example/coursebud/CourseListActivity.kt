package com.example.coursebud

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.SearchView
import android.widget.TextView
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class CourseListActivity : AppCompatActivity() {

    private lateinit var searchBarBack : TextView
    private lateinit var searchBar : SearchView
    private lateinit var results : TextView
    private lateinit var list : RecyclerView
    private lateinit var adapter : RecyclerView.Adapter<*>
    private lateinit var layoutManager : RecyclerView.LayoutManager

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_course_list)

        searchBarBack = findViewById(R.id.searchBarBack)
        searchBar = findViewById(R.id.searchBar)
        results = findViewById(R.id.results)
        list = findViewById(R.id.list)

        list.setHasFixedSize(true)
        // use a linear layout manager
        layoutManager = LinearLayoutManager(this@CourseListActivity, LinearLayoutManager.VERTICAL, false)
        list.layoutManager = layoutManager
        // create dataset, format should match what you specified 
        // in the CourseAdapter object
        var courses = mutableListOf<Course>()

        adapter = CourseAdapter(courses)
        list.adapter = adapter
    }
}