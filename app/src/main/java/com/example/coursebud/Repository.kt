package com.example.coursebud

class Repository private constructor() {
    companion object {
        val courseList = mutableListOf<Course>()
    }
}