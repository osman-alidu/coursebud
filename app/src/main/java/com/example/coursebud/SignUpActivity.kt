package com.example.coursebud

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.EditText
import android.widget.TextView
import okhttp3.Request
import java.io.IOException

class SignUpActivity : AppCompatActivity() {
    private lateinit var title : TextView
    private lateinit var annotation: TextView
    private lateinit var nameText : TextView
    private lateinit var nameInput : EditText
    private lateinit var emailText : TextView
    private lateinit var emailInput : EditText
    private lateinit var pwText : TextView
    private lateinit var pwInput : EditText
    private lateinit var gradText : TextView
    private lateinit var gradInput : EditText
    private lateinit var nextArrow : TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_sign_up)

        title = findViewById(R.id.title)
        annotation = findViewById(R.id.annotation)
        nameText = findViewById(R.id.nameText)
        nameInput = findViewById(R.id.nameInput)
        emailText = findViewById(R.id.emailText)
        pwText = findViewById(R.id.pwText)
        pwInput = findViewById(R.id.pwInput)
        gradText = findViewById(R.id.gradText)
        gradInput = findViewById(R.id.gradInput)
        nextArrow = findViewById(R.id.nextArrow)



       // registerUser()

        nextArrow.setOnClickListener {
            var intent = Intent(this, CourseListActivity::class.java)
            startActivity(intent)
        }
    }

//    private fun registerUser() {
//        lateinit var requestPost : Request
//        requestPost = Request.Builder().url(BASE_URL + "/api/users/register/)".build()
//                client.newCall(requestPost).enqueue(object : Callback {
//            override fun onFailure(call: Call, e: IOException) {
//                e.printStackTrace()
//                Log.d("debug", "failure" )
//            }
//
//            override fun onResponse(call: Call, response: Response) {
//                Log.d("debug", "On Response")
//                response.use {
//                    if (!it.isSuccessful) {
//                        throw IOException("Network call unsuccessful")
//                    }
//                    val courseList = courseListJsonAdapter.fromJson(response.body!!.string())!!
//                    for (course in courseList.courses) {
//                        courses.add(course)
//                    }
//                }
//            }
//        })
}