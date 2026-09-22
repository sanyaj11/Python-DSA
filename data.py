## profile will have name, age, course, marks, skills
##use list for marks, use set for skills

students = {
    "ST101": {
        "name": "Asha",
        "age": 20,
        "course": "Python",
        "marks": [78, 85, 91],  #why list? Ordered data
        "score": 42,
        "skills": {"python", "html"} #why sets? No Duplicates
    },
    "ST102": {
        "name": "Riya",
        "age": 20,
        "course": "DSA",
        "marks": [75, 80, 91],  #why list? Ordered data
        "score": 79,
        "skills": {"python", "html"} #why sets? No Duplicates
        },
    "ST103": {
        "name": "Neha",
        "age": 20,
        "course": "Python",
        "marks": [75, 85, 90],  #why list? Ordered data
        "score": 59,
        "skills": {"python", "html"} #why sets? No Duplicates
        },
    "ST104": {
        "name": "Pinky",
        "age": 21,
        "course": "Java",
        "marks": [88, 92, 95],
        "score": 91,
        "skills": {"java", "sql"}
        },
    "ST105": {
        "name": "Sara",
        "age": 22,
        "course": "DSA",
        "marks": [60, 65, 70],
        "score": 73,
        "skills": {"python", "c++"}
        },
    "ST106": {
        "name": "Vishal",
        "age": 20,
        "course": "Java",
        "marks": [50, 55, 45],
        "score": 39,
        "skills": {"java"}
        },
    "ST107": {
        "name": "Ariya",
        "age": 21,
        "course": "DSA",
        "marks": [80, 85, 88],
        "score": 91,  # duplicate score with ST104 (Pinky) -- good for tie-break testing
        "skills": {"python", "sql"}
        },
    "ST108": {
        "name": "Kabir",
        "age": 23,
        "course": "Python",
        "marks": [65, 70, 68],
        "score": 59,  # duplicate score with ST103 (Neha)
        "skills": {"python"}
        },
    "ST109": {
        "name": "Meera",
        "age": 20,
        "course": "Web Dev",
        "marks": [90, 95, 98],
        "score": 97,
        "skills": {"html", "css", "javascript"}
        },
    "ST110": {
        "name": "Zara",
        "age": 22,
        "course": "Java",
        "marks": [40, 42, 38],
        "score": 25,
        "skills": {"java", "sql"}
        },
    "ST111": {
        "name": "Aman",
        "age": 21,
        "course": "Web Dev",
        "marks": [70, 72, 75],
        "score": 73,  # duplicate score with ST105 (Sara)
        "skills": {"html", "css"}
        },
    "ST112": {
        "name": "Divya",
        "age": 20,
        "course": "DSA",
        "marks": [85, 88, 90],
        "score": 87,
        "skills": {"python", "c++"}
        }
}