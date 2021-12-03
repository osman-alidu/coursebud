package com.example.coursebud

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.EditText
import android.widget.TextView

class LoginActivity : AppCompatActivity() {
    private lateinit var loginTitle : TextView
    private lateinit var nameText : TextView
    private lateinit var nameInput : EditText
    private lateinit var pwText : TextView
    private lateinit var pwInput : EditText
    private lateinit var nextArrow : TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_login)
        loginTitle = findViewById(R.id.loginTitle)
        nameText = findViewById(R.id.nameText)
        nameInput = findViewById(R.id.nameInput)
        pwText = findViewById(R.id.pwText)
        pwInput = findViewById(R.id.pwInput)
        nextArrow = findViewById(R.id.nextArrow)

        //Need conditions: when the password and username match
        nextArrow.setOnClickListener {
            val intent = Intent(this, CourseListActivity::class.java)
            startActivity(intent)
        }
    }
}