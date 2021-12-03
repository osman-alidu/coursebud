package com.example.coursebud

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.TextView
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import okhttp3.Call
import okhttp3.Callback
import okhttp3.Request
import okhttp3.Response
import java.io.IOException

class ReviewPageActivity : AppCompatActivity() {

    private lateinit var addReviewButton: Button
    private lateinit var displayReviews: RecyclerView
    private lateinit var overallRatingText: TextView
    private lateinit var reviewsText: TextView
    private lateinit var adapter : ReviewAdapter
    private lateinit var layoutManager : RecyclerView.LayoutManager
    private var reviews = mutableListOf<Review>() //create dataset

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.review_page)

        addReviewButton = findViewById(R.id.addReviewButton)
        displayReviews = findViewById((R.id.displayReviews))
        overallRatingText = findViewById((R.id.overallRatingText))
        reviewsText = findViewById((R.id.reviewsText))

        displayReviews.setHasFixedSize(true)
        // use a linear layout manager
        layoutManager = LinearLayoutManager(this@ReviewPageActivity, LinearLayoutManager.VERTICAL, false)
        displayReviews.layoutManager = layoutManager

        // in the CourseAdapter object
        adapter = ReviewAdapter(reviews)
        displayReviews.adapter = adapter

        populateReviewList()

        addReviewButton.setOnClickListener {
            val intent = Intent(this, MakeReviewActivity::class.java)
            startActivity(intent)
        }
    }

    private fun populateReviewList() {

    }
}