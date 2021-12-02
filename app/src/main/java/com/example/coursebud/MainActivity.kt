package com.example.coursebud

import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.TextView

class MainActivity : AppCompatActivity() {
    private lateinit var appTitle : TextView
    private lateinit var signUpBtn : Button
    private lateinit var loginBtn : Button

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)

        appTitle = findViewById(R.id.appTitle)
        signUpBtn = findViewById(R.id.signUpBtn)
        loginBtn = findViewById(R.id.loginBtn)
    }
}