use("college_nosql");

db.createCollection("feedback");
db.feedback.insertMany([
  {
    student_id: 1,
    course_code: "CS101",
    semester: "2022-ODD",
    rating: 5,
    comments: "Excellent teaching.",
    tags: ["challenging", "well-structured", "good-examples"],
    submitted_at: new Date("2022-11-30T10:15:00Z"),
    attachments: [
      {
        filename: "notes.pdf",
        size_kb: 240
      }
    ]
  },
  {
    student_id: 2,
    course_code: "CS101",
    semester: "2022-ODD",
    rating: 4,
    comments: "Very useful course.",
    tags: ["challenging", "interesting"],
    submitted_at: new Date("2022-11-28T10:15:00Z"),
    attachments: [
      {
        filename: "assignment.pdf",
        size_kb: 180
      }
    ]
  },
  {
student_id:3,
course_code:"CS101",
semester:"2022-ODD",
rating:2,
comments:"Needs more practical examples.",
tags:["challenging","fast-paced"],
submitted_at:new Date("2022-11-25"),
attachments:[
{
filename:"feedback.docx",
size_kb:90
}
]
},

{
student_id:4,
course_code:"CS102",
semester:"2022-ODD",
rating:5,
comments:"Excellent DB concepts.",
tags:["database","easy"],
submitted_at:new Date("2022-11-26"),
attachments:[
{
filename:"dbnotes.pdf",
size_kb:150
}
]
},

{
student_id:5,
course_code:"CS102",
semester:"2022-ODD",
rating:3,
comments:"Good overall.",
tags:["database","examples"],
submitted_at:new Date("2022-11-24"),
attachments:[
{
filename:"lab.pdf",
size_kb:130
}
]
},

{
student_id:6,
course_code:"CS103",
semester:"2022-ODD",
rating:5,
comments:"Loved OOP.",
tags:["coding","interesting"],
submitted_at:new Date("2022-11-22"),
attachments:[
{
filename:"oop.pdf",
size_kb:140
}
]
},

{
student_id:7,
course_code:"EC101",
semester:"2022-ODD",
rating:1,
comments:"Very difficult.",
tags:["electronics","hard"],
submitted_at:new Date("2022-11-18"),
attachments:[
{
filename:"circuit.pdf",
size_kb:220
}
]
},

{
student_id:8,
course_code:"ME101",
semester:"2021-EVEN",
rating:4,
comments:"Interesting mechanics.",
tags:["mechanics","practical"],
submitted_at:new Date("2021-11-20"),
attachments:[
{
filename:"mech.pdf",
size_kb:170
}
]
},

{
student_id:9,
course_code:"CS101",
semester:"2021-EVEN",
rating:5,
comments:"Fantastic faculty.",
tags:["challenging","good-examples"],
submitted_at:new Date("2021-11-10")
},

{
student_id:10,
course_code:"CS103",
semester:"2022-ODD",
rating:2,
comments:"Assignments were difficult.",
tags:["coding","challenging"],
submitted_at:new Date("2022-11-21"),
attachments:[
{
filename:"assignment2.pdf",
size_kb:120
}
]
}

]);

// Verify Insert

db.feedback.countDocuments()
  // ============================================================
// TASK 2
// CRUD OPERATIONS
// ============================================================

// 65. Find all feedback with rating = 5
db.feedback.find({
  rating: 5
});

// ------------------------------------------------------------
// 66. Find CS101 feedback containing "challenging" tag
// ------------------------------------------------------------
db.feedback.find({
  course_code: "CS101",
  tags: "challenging"
});

// ------------------------------------------------------------
// 67. Projection (Exclude _id)
// ------------------------------------------------------------
db.feedback.find(
  {},
  {
    _id: 0,
    student_id: 1,
    course_code: 1,
    rating: 1
  }
);

// ------------------------------------------------------------
// 68. Add needs_review=true where rating < 3
// ------------------------------------------------------------
db.feedback.updateMany(
  {
    rating: { $lt: 3 }
  },
  {
    $set: {
      needs_review: true
    }
  }
);

// Verify
db.feedback.find({
  needs_review: true
});

// ------------------------------------------------------------
// 69. Push "reviewed" tag
// ------------------------------------------------------------
db.feedback.updateMany(
  {
    needs_review: true
  },
  {
    $push: {
      tags: "reviewed"
    }
  }
);

// Verify
db.feedback.find({
  needs_review: true
});

// ------------------------------------------------------------
// 70. Delete semester = 2021-EVEN
// ------------------------------------------------------------
db.feedback.deleteMany({
  semester: "2021-EVEN"
});

// Verify
db.feedback.countDocuments();
// ============================================================
// TASK 3
// Aggregation Pipeline
// ============================================================

// ------------------------------------------------------------
// 71 & 72
// Average Rating Per Course
// ------------------------------------------------------------
db.feedback.aggregate([
  {
    $match: {
      semester: "2022-ODD"
    }
  },
  {
    $group: {
      _id: "$course_code",
      avg_rating: {
        $avg: "$rating"
      },
      total_feedback: {
        $sum: 1
      }
    }
  },
  {
    $project: {
      _id: 0,
      course_code: "$_id",
      average_rating: {
        $round: ["$avg_rating", 1]
      },
      total_feedback: 1
    }
  },
  {
    $sort: {
      average_rating: -1
    }
  }
]);