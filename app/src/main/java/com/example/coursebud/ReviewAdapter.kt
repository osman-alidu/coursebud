package com.example.coursebud

import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.recyclerview.widget.RecyclerView

class ReviewAdapter(private val reviews: List<Review>) : RecyclerView.Adapter<ReviewAdapter.ViewHolder>()  {

    class ViewHolder internal constructor(itemView : View) : RecyclerView.ViewHolder(itemView) {
        val comment : TextView = itemView.findViewById(R.id.comment)
    }

    override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): ReviewAdapter.ViewHolder {
        val view = LayoutInflater.from(parent.context).inflate(R.layout.review_cell, parent, false) as View
        return ReviewAdapter.ViewHolder(view)
    }

    override fun onBindViewHolder(holder: ReviewAdapter.ViewHolder, position: Int) {
        val review = reviews[position]
        holder.comment.text = review.comment
    }

    override fun getItemCount(): Int {
        return reviews.size
    }
}