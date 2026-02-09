# AI-Powered Todo Application - Development Guide

## Project Information

This document serves as a comprehensive guide for the AI-Powered Todo Application developed for the hackathon.

## Quick Start

### Prerequisites
- Node.js 18+ and npm
- Python 3.11+
- Google Gemini API key

### Backend Setup

1. Navigate to backend directory:
```bash
cd backend
```

2. Create virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create `.env` file:
```
GEMINI_API_KEY=your_api_key_here
JWT_SECRET_KEY=your_secret_key_here
DATABASE_URL=sqlite:///./todo.db
```

5. Run the server:
```bash
uvicorn main:app --reload
```

Backend will run on `http://localhost:8000`

### Frontend Setup

1. Navigate to frontend directory:
```bash
cd frontend
```

2. Install dependencies:
```bash
npm install
```

3. Create `.env.local` file:
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

4. Run development server:
```bash
npm run dev
```

Frontend will run on `http://localhost:3000`

## Project Structure

```
d:\Hackathon/
├── backend/
│   ├── main.py              # FastAPI application entry
│   ├── auth.py              # Authentication logic
│   ├── database.py          # Database configuration
│   ├── models.py            # SQLModel schemas
│   ├── mcp_tools.py         # AI tool definitions
│   ├── routes/
│   │   ├── auth.py          # Auth endpoints
│   │   ├── tasks.py         # Task endpoints
│   │   └── chat.py          # Chat endpoints
│   ├── requirements.txt     # Python dependencies
│   └── .env                 # Environment variables
│
├── frontend/
│   ├── app/
│   │   ├── page.tsx         # Landing/Login page
│   │   ├── layout.tsx       # Root layout
│   │   ├── globals.css      # Global styles
│   │   ├── dashboard/
│   │   │   └── page.tsx     # Dashboard page
│   │   └── chat/
│   │       └── page.tsx     # Chat interface
│   ├── lib/
│   │   ├── auth.ts          # Auth utilities
│   │   └── api.ts           # API client
│   ├── package.json         # Node dependencies
│   └── .env.local           # Environment variables
│
├── README.md                # Project documentation
├── HOW-TO-TEST.md          # Testing guide
└── constitution.md          # Project constitution
```

## Features Overview

### 1. Authentication System
- Secure user registration and login
- JWT-based session management
- Password hashing with bcrypt
- Protected routes and API endpoints

### 2. Task Management Dashboard
- Create, edit, and delete tasks
- Mark tasks as complete/incomplete
- Filter tasks (All, Active, Completed)
- Real-time task statistics
- Productivity insights
- Modern UI with glass morphism

### 3. AI Chat Interface
- Natural language task creation
- Conversational AI assistant powered by Gemini
- Context-aware responses
- Task management through chat
- Conversation history

### 4. Modern UI/UX
- Responsive design for all devices
- Dark theme with vibrant gradients
- Smooth animations and transitions
- Glass morphism effects
- Comprehensive dashboard with stats cards
- Productivity insights and tips

## API Documentation

### Authentication Endpoints

**POST /auth/signup**
```json
Request:
{
  "email": "user@example.com",
  "password": "securepassword",
  "name": "John Doe"
}

Response:
{
  "access_token": "jwt_token_here",
  "token_type": "bearer",
  "user": {
    "id": "uuid",
    "email": "user@example.com",
    "name": "John Doe"
  }
}
```

**POST /auth/signin**
```json
Request:
{
  "email": "user@example.com",
  "password": "securepassword"
}

Response:
{
  "access_token": "jwt_token_here",
  "token_type": "bearer",
  "user": {...}
}
```

### Task Endpoints

**GET /tasks/{user_id}**
- Returns all tasks for the user
- Requires authentication

**POST /tasks/{user_id}**
```json
Request:
{
  "title": "Complete project",
  "description": "Finish the hackathon project"
}

Response:
{
  "id": 1,
  "user_id": "uuid",
  "title": "Complete project",
  "description": "Finish the hackathon project",
  "completed": false,
  "created_at": "2024-01-09T12:00:00",
  "updated_at": "2024-01-09T12:00:00"
}
```

**POST /tasks/{user_id}/{task_id}/toggle**
- Toggles task completion status
- Returns updated task

**DELETE /tasks/{user_id}/{task_id}**
- Deletes a task
- Returns success message

### Chat Endpoints

**POST /chat/{user_id}/chat**
```json
Request:
{
  "message": "Create a task to buy groceries",
  "conversation_id": 1  // optional
}

Response:
{
  "response": "I've created a task for you to buy groceries.",
  "conversation_id": 1
}
```

## Technology Stack Details

### Frontend Technologies
- **Next.js 16.1.1** - React framework with server-side rendering
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS v4** - Utility-first CSS framework
- **React Hot Toast** - Toast notifications
- **Canvas Confetti** - Celebration animations

### Backend Technologies
- **FastAPI** - Modern Python web framework
- **SQLModel** - SQL database ORM
- **SQLite** - Lightweight database
- **Pydantic** - Data validation
- **Python-Jose** - JWT token handling
- **Passlib** - Password hashing
- **Google Generative AI** - Gemini AI integration

## Development Best Practices

1. **Code Organization**
   - Separate concerns (routes, models, utilities)
   - Use TypeScript for type safety
   - Follow REST API conventions

2. **Security**
   - Never commit `.env` files
   - Use environment variables for secrets
   - Implement proper authentication
   - Validate all user inputs

3. **UI/UX**
   - Maintain consistent design language
   - Provide user feedback (toasts, loading states)
   - Ensure responsive design
   - Use meaningful animations

4. **Error Handling**
   - Graceful error messages
   - Try-catch blocks for async operations
   - Proper HTTP status codes
   - User-friendly error displays

## Testing

See `HOW-TO-TEST.md` for detailed testing instructions.

## Troubleshooting

### Backend Issues
- **Port already in use**: Change port in uvicorn command
- **Database errors**: Delete `todo.db` and restart
- **API key errors**: Verify `GEMINI_API_KEY` in `.env`

### Frontend Issues
- **Build errors**: Clear `.next` folder and rebuild
- **API connection**: Verify `NEXT_PUBLIC_API_URL` in `.env.local`
- **Styling issues**: Clear browser cache

## Contributing

This is a hackathon project. For improvements:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Support

For questions or issues, refer to:
- `README.md` - General documentation
- `HOW-TO-TEST.md` - Testing guide
- `constitution.md` - Project overview

## License

MIT License - Open source hackathon project.
