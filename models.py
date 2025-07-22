from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from app import db

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Time, nullable=False)
    notes = db.Column(db.Text, nullable=True)
    google_event_id = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __init__(self, name, phone, email, date, time, notes=None, google_event_id=None):
        self.name = name
        self.phone = phone
        self.email = email
        self.date = date
        self.time = time
        self.notes = notes
        self.google_event_id = google_event_id

class Settings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    booking_enabled = db.Column(db.Boolean, default=True)
    slot_duration = db.Column(db.Integer, default=30)  # 분 단위
    admin_password_hash = db.Column(db.String(255))
    start_time = db.Column(db.String(5), default='09:00')  # HH:MM
    end_time = db.Column(db.String(5), default='18:00')    # HH:MM
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __init__(self, booking_enabled=True, slot_duration=30, admin_password_hash=None, start_time='09:00', end_time='18:00'):
        self.booking_enabled = booking_enabled
        self.slot_duration = slot_duration
        self.admin_password_hash = admin_password_hash
        self.start_time = start_time
        self.end_time = end_time
    
    def set_admin_password(self, password):
        self.admin_password_hash = generate_password_hash(password)
    
    def check_admin_password(self, password):
        return check_password_hash(self.admin_password_hash, password)

class GoogleToken(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.Text, nullable=False)
    refresh_token = db.Column(db.Text, nullable=True)
    token_uri = db.Column(db.String(255), nullable=False)
    client_id = db.Column(db.String(255), nullable=False)
    client_secret = db.Column(db.String(255), nullable=False)
    scopes = db.Column(db.Text, nullable=False)  # JSON string
    expires_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def __init__(self, token, token_uri, client_id, client_secret, scopes, refresh_token=None, expires_at=None):
        self.token = token
        self.refresh_token = refresh_token
        self.token_uri = token_uri
        self.client_id = client_id
        self.client_secret = client_secret
        self.scopes = scopes
        self.expires_at = expires_at


class DateTimeSlot(db.Model):
    """날짜별 시간 슬롯 관리"""
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)  # 특정 날짜
    time = db.Column(db.String(5), nullable=False)  # HH:MM 형식
    duration = db.Column(db.Integer, default=20)  # 분 단위 (20분, 30분, 60분 등)
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<DateTimeSlot {self.date} {self.time} ({self.duration}분)>'


class TimeSlot(db.Model):
    """기본 시간 슬롯 템플릿 (전역 사용)"""
    id = db.Column(db.Integer, primary_key=True)
    time = db.Column(db.String(5), nullable=False)  # HH:MM 형식
    duration = db.Column(db.Integer, default=20)  # 분 단위
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<TimeSlot {self.time} ({self.duration}분)>'