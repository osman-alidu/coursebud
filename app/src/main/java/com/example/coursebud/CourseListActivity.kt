package com.example.coursebud

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView

class CourseListActivity : AppCompatActivity() {

    private lateinit var recyclerView : RecyclerView
    private lateinit var mAdapter : RecyclerView.Adapter<*>
    private lateinit var layoutManager : RecyclerView.LayoutManager

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_course_list)

        recyclerView = findViewById<RecyclerView>(R.id.list)

        recyclerView.setHasFixedSize(true)
        // use a linear layout manager
        layoutManager = LinearLayoutManager(this@CourseListActivity)
        recyclerView.layoutManager = layoutManager
        // create dataset, format should match what you specified 
        // in the CourseAdapter object
        var courses = mutableListOf<String>()

        mAdapter = CourseAdapter(courses)
        recyclerView.adapter = mAdapter
    }
}