package com.example.coursebud

import com.squareup.moshi.JsonClass

@JsonClass(generateAdapter = true)
data class Course(
    val id:Int,
    val code:String,
    val name:String,
    val rating:Int,
    val comments: List<String>
    )
