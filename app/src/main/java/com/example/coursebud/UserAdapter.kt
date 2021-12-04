//package com.example.coursebud
//
//import android.view.LayoutInflater
//import android.view.View
//import android.view.ViewGroup
//import android.widget.TextView
//import androidx.recyclerview.widget.RecyclerView
//import org.w3c.dom.Text
//
//class UserAdapter {
//    class UserAdapter(private val Users: List<User>) : RecyclerView.Adapter<UserAdapter.ViewHolder>()  {
//
//        class ViewHolder internal constructor(itemView : View) : RecyclerView.ViewHolder(itemView) {
//            val comment : TextView = itemView.findViewById(R.id.comment)
//            val email : TextView = itemView.findViewById(R.id.emailText)
//        }
//
//        override fun onCreateViewHolder(parent: ViewGroup, viewType: Int): UserAdapter.ViewHolder {
//            val view = LayoutInflater.from(parent.context).inflate(R.layout.User_cell, parent, false) as View
//            return UserAdapter.ViewHolder(view)
//        }
//
//        override fun onBindViewHolder(holder: UserAdapter.ViewHolder, position: Int) {
//            val User = Users[position]
//            holder.comment.text = User.comment
//        }
//
//        override fun getItemCount(): Int {
//            return Users.size
//        }
//    }
//}