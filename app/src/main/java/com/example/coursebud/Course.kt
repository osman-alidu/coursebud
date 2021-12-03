package com.example.coursebud

import com.squareup.moshi.JsonClass

@JsonClass(generateAdapter = true)
data class Course(
    val rating:Int,
    val courseName:String,
    val reviewNumber:String,
    val code:String
    )
