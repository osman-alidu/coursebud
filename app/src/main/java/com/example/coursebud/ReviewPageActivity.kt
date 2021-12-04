package com.example.coursebud

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.TextView
import androidx.recyclerview.widget.LinearLayoutManager
import androidx.recyclerview.widget.RecyclerView
import com.squareup.moshi.JsonAdapter
import com.squareup.moshi.Moshi
import com.squareup.moshi.Types
import com.squareup.moshi.kotlin.reflect.KotlinJsonAdapterFactory
import okhttp3.*
import java.io.IOException

class ReviewPageActivity : AppCompatActivity() {

    private lateinit var addReviewButton: Button
    private lateinit var displayReviews: RecyclerView
    private lateinit var overallRatingText: TextView
    private lateinit var reviewsText: TextView
    private lateinit var adapter : ReviewAdapter
    private lateinit var layoutManager : RecyclerView.LayoutManager
    private lateinit var courseName : TextView
    private lateinit var courseCode : TextView
    private lateinit var overallRating : TextView
    private var reviews = mutableListOf<Review>() //create dataset

    private val client = OkHttpClient()
    private val moshi = Moshi.Builder().addLast(KotlinJsonAdapterFactory()).build()
    private val reviewJsonAdapter = moshi.adapter(Review::class.java)
    private var id = ""
    private val reviewListType = Types.newParameterizedType(ReviewWrapper::class.java, ReviewWrapper::class.java)
    private val reviewListJsonAdapter : JsonAdapter<ReviewWrapper> = moshi.adapter(reviewListType)

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.review_page)

        courseName = findViewById(R.id.courseName)
        courseCode = findViewById(R.id.courseCode)
        overallRating = findViewById(R.id.rating)
        addReviewButton = findViewById(R.id.addReviewButton)
        displayReviews = findViewById((R.id.displayReviews))
        overallRatingText = findViewById((R.id.overallRatingText))
        reviewsText = findViewById((R.id.reviewsText))

        var name = intent.extras?.getString("name")
        var rating = intent.extras?.getString("rating")
        var code = intent.extras?.getString("code")
        id = intent.extras?.getString("id").toString()


        courseName.setText(name)
        courseCode.setText(code)
        overallRating.setText(rating)


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
        lateinit var requestGet: Request
        requestGet = Request.Builder().url(BASE_URL + "/api/courses/" + id + "/comments").build()
        client.newCall(requestGet).enqueue(object : Callback {
            override fun onFailure(call: Call, e: IOException) {
                e.printStackTrace()
                Log.d("debug", "failure")
            }

            override fun onResponse(call: Call, response: Response) {
                Log.d("debug", "On Response")
                response.use {
                    if (!it.isSuccessful) {
                        throw IOException("Network call unsuccessful")
                    }
                    val reviewList = reviewListJsonAdapter.fromJson(response.body!!.string())!!
                    for (review in reviewList.comments) {
                        reviews.add(review)
                    }
                    adapter = ReviewAdapter(reviews)
                    runOnUiThread {
                        displayReviews.adapter = adapter
                    }
                }
            }
        })

    }
}