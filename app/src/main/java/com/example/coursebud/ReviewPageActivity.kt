package com.example.coursebud

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class ReviewPageActivity : AppCompatActivity() {

    private lateinit var addReviewButton: Button
    private lateinit var displayReviews: RecyclerView
    private lateinit var overallRatingText: TextView
    private lateinit var reviewsText: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.review_page)

        addReviewButton = findViewById(R.id.addReviewButton)
        displayReviews = findViewById((R.id.displayReviews))
        overallRatingText = findViewById((R.id.overallRatingText))
        reviewsText = findViewById((R.id.reviewsText))


        addReviewButton.setOnClickListener {
            val intent = Intent(this, MakeReviewActivity::class.java)
            startActivity(intent)
        }
    }
}