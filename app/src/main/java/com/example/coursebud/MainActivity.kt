package com.example.coursebud

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    private lateinit var appTitle : TextView
    private lateinit var intro : TextView
    private lateinit var loginText : TextView
    private lateinit var loginBtn : Button
    private lateinit var signupText : TextView
    private lateinit var signupBtn : Button


    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        appTitle = findViewById(R.id.appTitle)
        intro = findViewById(R.id.intro)
        loginText = findViewById(R.id.loginText)
        loginBtn = findViewById(R.id.loginBtn)
        signupText = findViewById(R.id.signupText)
        signupBtn = findViewById(R.id.signUpBtn)

        loginBtn.setOnClickListener {

        }

        signupBtn.setOnClickListener {

        }
    }
}