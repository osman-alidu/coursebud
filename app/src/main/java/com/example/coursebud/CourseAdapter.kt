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

        val index : TextView = itemView.findViewById(R.id.index)
        val level : TextView = itemView.findViewById(R.id.level)
        val split_line : TextView = itemView.findViewById(R.id.split_line)
        val course_number : TextView = itemView.findViewById(R.id.course_number)
        val stars : TextView = itemView.findViewById(R.id.stars)
        val review_number : TextView = itemView.findViewById(R.id.review_number)
        val reviews : TextView = itemView.findViewById(R.id.reviews)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.course_cell, parent, false) as View
        return ViewHolder(view)
    }

    override fun onBindViewHolder(holder: ViewHolder, position: Int) {
        val course = courses[position]
        holder.index.text = course.index
        holder.level.text = course.level
        holder.split_line.text = course.split_line
        holder.course_number.text = course.course_number
        holder.stars.text = course.stars
        holder.review_number.text = course.review_number
        holder.reviews.text = course.reviews
    }

    override fun getItemCount(): Int {
        return courses.size
    }
}