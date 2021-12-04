package com.example.coursebud

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.Button
import android.widget.EditText
import android.widget.TextView
import com.squareup.moshi.Moshi
import com.squareup.moshi.kotlin.reflect.KotlinJsonAdapterFactory
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.runBlocking
import kotlinx.coroutines.withContext
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.RequestBody.Companion.toRequestBody
import org.w3c.dom.Text
import java.io.IOException

class  MakeReviewActivity : AppCompatActivity() {

    private lateinit var submitReviewButton: Button
    private lateinit var leaveReviewText: TextView
    private lateinit var writeReviewBox: EditText
    private var id = ""
    private val moshi = Moshi.Builder().addLast(KotlinJsonAdapterFactory()).build()
    private val reviewJsonAdapter = moshi.adapter(Review::class.java)
    private val client = OkHttpClient()

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.make_review)

        submitReviewButton = findViewById(R.id.submitReviewButton)
        leaveReviewText = findViewById(R.id.leaveReviewText)
        writeReviewBox = findViewById(R.id.writeReviewBox)

        var name = intent.extras?.getString("name")
        var rating = intent.extras?.getString("rating")
        var code = intent.extras?.getString("code")
        id = intent.extras?.getString("id").toString()
        // var reviewList = intent.extras?.getStringArrayList("reviews")


        submitReviewButton.setOnClickListener {


            runBlocking {
                withContext(Dispatchers.IO) {
                    val newReview = Review(writeReviewBox.text.toString())
                    postReviewToCourse(newReview)
                }
            }

            val intent = Intent(this, ReviewPageActivity::class.java).apply{
                putExtra("name", name)
                putExtra("code", code)
                putExtra("rating", rating)
                putExtra("id", id)
            }
            startActivity(intent)
            updateCourse()
        }


    }

    private fun postReviewToCourse(newReview : Review) {
        val requestPost = Request.Builder().url(BASE_URL + "/api/users/"+id+"/comments/")
            .post(reviewJsonAdapter.toJson(newReview).toRequestBody(("application/json; charset=utf-8").toMediaType())).build()
        client.newCall(requestPost).execute().use {
            if (!it.isSuccessful) {
                // handle unsuccessful response
                Log.e("NETWORK_ERROR", it.message)
                throw IOException("Post unsuccessful")
            }
            val responseString = it.body!!.string()
            Log.d("NETWORK_RESPONSE", responseString)
        }


    }

    private fun updateCourse() {

    }
}