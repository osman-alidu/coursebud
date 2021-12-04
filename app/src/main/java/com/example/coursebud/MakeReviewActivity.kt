package com.example.coursebud

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import org.w3c.dom.Text

class  MakeReviewActivity : AppCompatActivity() {

    private lateinit var submitReviewButton: Button
    private lateinit var leaveReviewText: Text
    private lateinit var writeReviewBox: TextView


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.make_review)

        submitReviewButton = findViewById(R.id.submitReviewButton)
        leaveReviewText = findViewById(R.id.leaveReviewText)
        writeReviewBox = findViewById(R.id.writeReviewBox)

        submitReviewButton.setOnClickListener {

            //val editedReview = N(taskEditBody.text.toString(), id!!, poster, taskEditTitle.text.toString())
            //Repository.noteList.add(editedNote)

            //val intent = Intent(this, CloudNotesActivity::class.java)
            //startActivity(intent)
            //updateCourse()
        }


    }

    private fun updateCourse() {

    }

    }

//    private fun updateNote(newNote: Note) {
//        val requestPost = Request.Builder().url(BASE_URL + "/api/users/" + user_id.toString() + course_id.toString() + "/comments/")
//            .post(noteJsonAdapter.toJson(newComment).toRequestBody(("application/json; charset=utf-8").toMediaType())).build()
//        client.newCall(requestPost).execute().use {
//            if (!it.isSuccessful) {
//    // handle unsuccessful response
//                Log.e("NETWORK_ERROR", it.message)
//                throw IOException("Post unsuccessful")
//            }
//            val responseString = it.body!!.string()
//            Log.d("NETWORK_RESPONSE", responseString)
//        }
//    }
