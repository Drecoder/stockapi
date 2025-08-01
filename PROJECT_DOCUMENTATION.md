# StockAPI + React Frontend — Project Documentation

## 1. Executive Summary

This project is a full-stack stock data dashboard featuring a React frontend and a Django REST backend.
It pulls live stock data from Yahoo Finance and will eventually integrate SEC EDGAR filings and AI-generated insights.

Key goals:
- Provide real-time stock quotes
- Manage user watchlists
- Support historical data visualization and advanced analytics

## 2. System Architecture

![System Architecture](docs/system-architecture.png)

### Components:
- **React Frontend:** User interface for searching stocks and managing watchlists.
- **Django REST API:** Backend serving stock data and persisting user data.
- **External APIs:** Yahoo Finance and SEC EDGAR for financial data.
- **Database:** PostgreSQL or SQLite for persistence.

Data flows from external APIs to Django, then to React, with persistent storage.

## 3. Scope of Work

### Core Features
- Stock quote retrieval and normalization
- Watchlist CRUD with persistent storage
- REST API endpoints for frontend integration
- Responsive UI/UX with live updates

### Future Features
- SEC EDGAR filing integration
- AI-based stock analysis and summaries
- User authentication and preferences
- Push notifications for stock alerts

## 4. Sprint Plan (2-Week Sprints)

| Sprint | Goals                                   | Deliverables                            |
|--------|-----------------------------------------|---------------------------------------|
| 1      | Backend setup & Yahoo Finance API       | Working REST endpoint, CORS enabled   |
| 2      | React frontend basics                    | Stock search and display               |
| 3      | Watchlist management                     | Full CRUD API and UI                   |
| 4      | Historical data & charting               | Backend storage + frontend charts      |
| 5      | Advanced features                        | AI integration, SEC EDGAR integration  |

## 5. Backlog / Future Enhancements
- AI-generated stock reports
- SEC filings deep integration
- Authentication & user profiles
- Real-time push notifications
- Performance improvements & caching

---

## 6. How to Run Locally

1. Clone the repo  
2. Install backend dependencies: `pip install -r requirements.txt`  
3. Run Django server: `python manage.py runserver 4000`  
4. In a separate terminal, start React frontend: `npm start`  
5. Open browser at `http://localhost:3000`

---

## 7. Contact & Contribution

Open to contributions, feedback, and suggestions. Reach out via GitHub issues or email.

---

