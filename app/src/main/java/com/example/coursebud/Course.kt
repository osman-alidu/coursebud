package com.example.coursebud

import com.squareup.moshi.JsonClass

@JsonClass(generateAdapter = true)
data class Course(
    val rating:Int,
    val name:String,
    val comments: List<String>,
    val code:String
    )
