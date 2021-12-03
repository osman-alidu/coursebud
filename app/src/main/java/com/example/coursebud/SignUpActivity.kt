package com.example.coursebud

import android.content.Intent
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.EditText
import android.widget.TextView

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

        nextArrow.setOnClickListener {
            var intent = Intent(this, CourseListActivity::class.java)
            startActivity(intent)
        }
    }
}