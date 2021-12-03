package com.example.coursebud

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.SearchView
import android.widget.TextView
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.squareup.moshi.JsonAdapter
import com.squareup.moshi.Moshi
import com.squareup.moshi.Types
import com.squareup.moshi.kotlin.reflect.KotlinJsonAdapterFactory
import okhttp3.*
import java.io.IOException

class CourseListActivity : AppCompatActivity() {

    private lateinit var searchBarBack : TextView
    private lateinit var searchBar : SearchView
    private lateinit var results : TextView
    private lateinit var list : RecyclerView
    private lateinit var adapter : CourseAdapter
    private lateinit var layoutManager : RecyclerView.LayoutManager

    private var courses = mutableListOf<Course>() //create dataset
    private val client = OkHttpClient()
    private val moshi = Moshi.Builder().addLast(KotlinJsonAdapterFactory()).build()
    private val courseJsonAdapter = moshi.adapter(Course::class.java)
    private val courseListType = Types.newParameterizedType(List::class.java, Course::class.java)
    private val courseListJsonAdapter : JsonAdapter<List<Course>> = moshi.adapter(courseListType)


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

        // in the CourseAdapter object
        adapter = CourseAdapter(courses)
        list.adapter = adapter

        populateCourseList()
    }

    private fun populateCourseList() {
        val requestGet = Request.Builder().url(BASE_URL + "api/courses").build()
        client.newCall(requestGet).enqueue(object: Callback {
            override fun onFailure(call: Call, e: IOException) {
                e.printStackTrace()
            }

            override fun onResponse(call: Call, response: Response) {
                response.use {
                    if (!it.isSuccessful) {
                        throw IOException("Network call unsuccessful")
                    }
                    val courseList = courseListJsonAdapter.fromJson(response.body!!.string())!!
                    for (course in courseList) {
                        courses.add(course)
                    }
                    adapter = CourseAdapter(courses)
                    runOnUiThread {
                        list.adapter = adapter
                    }
                }
            }
        })
    }
}