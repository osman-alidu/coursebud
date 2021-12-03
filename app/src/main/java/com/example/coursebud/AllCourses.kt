package com.example.coursebud

import com.squareup.moshi.JsonClass

@JsonClass(generateAdapter = true)
data class AllCourses (
    val courses : List<Course>
)
