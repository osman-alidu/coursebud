package com.example.coursebud

import com.squareup.moshi.JsonClass

@JsonClass(generateAdapter = true)
data class ReviewWrapper (
    val comments : List<Review>
)
