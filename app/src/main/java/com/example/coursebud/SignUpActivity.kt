package com.example.coursebud

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.util.Log
import android.widget.EditText
import android.widget.TextView
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

        private fun registerNewUser() {
            val requestPost = Request.Builder().url(BASE_URL + "/api/users/register/")
                .post(nameInput, emailInput, pwInput, gradInput).toRequestBody(("application/json; charset=utf-8").toMediaType())).build()
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

        registerNewUser()

        nextArrow.setOnClickListener {
            var intent = Intent(this, CourseListActivity::class.java)
            startActivity(intent)
        }
    }
}