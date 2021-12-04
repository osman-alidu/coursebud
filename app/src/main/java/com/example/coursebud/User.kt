package com.example.coursebud

import com.squareup.moshi.JsonClass

@JsonClass(generateAdapter = true)
data class User(
    val id:Int,
    val comments:String,
    val email:String,
    val username:String,
    val password:String
)