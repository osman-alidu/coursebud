package com.example.coursebud

import com.squareup.moshi.JsonClass

@JsonClass(generateAdapter = true)

data class Review (
    val comment : String
)
