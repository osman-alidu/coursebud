package com.example.coursebud

import android.content.Intent
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.ImageView
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class CourseAdapter(private val courses: List<Course>) : RecyclerView.Adapter<CourseAdapter.ViewHolder>() {

    class ViewHolder internal constructor(itemView : View) : RecyclerView.ViewHolder(itemView) {

        val rating : TextView = itemView.findViewById(R.id.rating)
        val courseName : TextView = itemView.findViewById(R.id.courseName)
        val reviewNumber : TextView = itemView.findViewById(R.id.review_number)
        val reviews : TextView = itemView.findViewById(R.id.reviews)
        val code : TextView = itemView.findViewById(R.id.code)

    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.course_cell, parent, false) as View
        return ViewHolder(view)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        val course = courses[position]
        holder.rating.text = course.rating.toString()
        holder.courseName.text = course.courseName
        holder.reviewNumber.text = course.reviewNumber
        holder.reviews.text = "reviews"
        holder.code.text = course.code

    }

    override fun getItemCount(): Int {
        return courses.size
    }
}