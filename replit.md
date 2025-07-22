# Booking System - Project Guide

## Overview

This is a Flask-based booking system that allows users to make appointments through a web interface. The system integrates with Google Calendar for automatic event creation and provides an admin panel for managing bookings and system settings.

## User Preferences

Preferred communication style: Simple, everyday language.
Admin password: dnlxkr1004
Design preference: Orange-based color theme
Time management: Admin-controlled time slots (no Google Calendar integration)

## System Architecture

### Backend Architecture
- **Framework**: Flask (Python web framework)
- **Database**: SQLAlchemy ORM with support for SQLite (development) and PostgreSQL (production)
- **Authentication**: Session-based admin authentication with password hashing
- **API Integration**: Google Calendar API for event synchronization
- **Template Engine**: Jinja2 for server-side rendering

### Frontend Architecture
- **UI Framework**: Bootstrap 5 with custom orange theme
- **JavaScript**: Vanilla JavaScript for calendar interface and interactive features
- **Icons**: Bootstrap Icons
- **Styling**: Orange-based theme with gradients and modern design elements

### Project Structure
```
├── app.py              # Flask application setup and configuration
├── main.py            # Application entry point
├── config.py          # Configuration settings
├── models.py          # Database models
├── routes/            # Route handlers organized by functionality
│   ├── main.py       # Main booking routes
│   ├── admin.py      # Admin panel routes
│   └── auth.py       # Google OAuth routes
├── services/         # Business logic services
│   ├── booking_service.py    # Booking management logic
│   └── calendar_service.py   # Google Calendar integration
├── templates/        # Jinja2 templates
└── static/          # Static assets (CSS, JS)
```

## Key Components

### Database Models
1. **Booking**: Core booking entity with customer info, datetime
2. **Settings**: System configuration (slot duration, operating hours, admin password)
3. **TimeSlot**: Admin-managed time slots with activation status
4. **GoogleToken**: Legacy OAuth2 tokens (not used per user request)

### Services Layer
1. **BookingService**: Handles admin-defined slot retrieval, booking creation, and validation
2. **CalendarService**: Removed per user request (no Google Calendar integration)

### Route Handlers
1. **Main Routes**: Public booking interface with calendar API endpoints
2. **Admin Routes**: Protected admin panel with time slot management
3. **Auth Routes**: Legacy Google OAuth2 routes (not used)

## Data Flow

### Booking Creation Flow
1. User selects date from calendar grid interface (excludes weekends and past dates)
2. System displays admin-defined time slots with availability status
3. User selects available time slot and fills booking form
4. System creates booking record in database
5. Success page displays booking confirmation

### Admin Management Flow
1. Admin authenticates with password-based login (password: dnlxkr1004)
2. Dashboard displays booking statistics and system status
3. Admin can view/filter bookings and export to CSV
4. Time Slots page allows adding/removing/toggling available booking times
5. Settings page allows configuration of system preferences

### Google Calendar Integration
1. Admin initiates OAuth2 flow through authorization endpoint
2. System exchanges authorization code for access tokens
3. Tokens stored in database for API calls
4. Calendar events created automatically for new bookings
5. Email invitations sent to booking contact if provided

## External Dependencies

### Google Services
- **Google Calendar API**: Event creation and management
- **Google OAuth2**: Authentication and authorization
- **Required Scopes**: 
  - `calendar.readonly`: View calendar information
  - `calendar.events`: Create and manage events

### Python Packages
- **Flask**: Web framework and extensions (SQLAlchemy)
- **Werkzeug**: Security utilities for password hashing
- **Google API Client**: Calendar API integration
- **Bootstrap**: Frontend UI framework (CDN)

### Environment Variables
- `SESSION_SECRET`: Flask session encryption key
- `DATABASE_URL`: Database connection string
- `GOOGLE_CLIENT_ID`: OAuth2 client identifier
- `GOOGLE_CLIENT_SECRET`: OAuth2 client secret

## Deployment Strategy

### Development Setup
- Uses SQLite database for local development
- Debug mode enabled for development server
- Environment variables with development defaults

### Production Considerations
- Supports PostgreSQL through DATABASE_URL environment variable
- ProxyFix middleware for reverse proxy compatibility
- Connection pooling and health checks configured
- Secure session management with production secret keys

### Key Features
1. **Calendar Interface**: Interactive monthly calendar with date/time selection
2. **Admin Panel**: Complete booking and time slot management system
3. **Custom Time Slots**: Admin-controlled available booking times
4. **Data Export**: CSV export functionality for bookings
5. **Orange Theme**: Modern, responsive design with orange color palette
6. **Session Security**: Secure admin authentication with password hashing

## Recent Changes (July 2025)
- Removed Google Calendar integration per user request
- Implemented calendar-style date selection interface
- Added TimeSlot model for admin-controlled time management
- Created orange-based theme with modern gradients and styling
- Updated admin dashboard with time slot management functionality
- Changed admin password to user-specified value
- Added 20-minute time slot intervals alongside existing options
- Implemented DateTimeSlot model for date-specific time registration
- UI fixes applied after theme changes to maintain proper functionality

The system is designed to be easily deployable on cloud platforms with minimal configuration changes, supporting both SQLite for development and PostgreSQL for production environments.