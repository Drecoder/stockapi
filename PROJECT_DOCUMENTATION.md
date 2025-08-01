# StockAPI + React Frontend — Project Documentation

## 1. Executive Summary

This project is a full-stack stock and macroeconomic data dashboard featuring a React frontend and a Django REST backend.  
It pulls live stock data from **Yahoo Finance**, **macroeconomic indicators from FRED**, and **SEC EDGAR filings** for corporate disclosures.  
It also integrates **Gemini AI** for generating intelligent financial insights and summaries.  

Key goals:
- Provide real-time stock quotes and macroeconomic indicators
- Manage user watchlists
- Support historical data visualization and advanced analytics
- Leverage AI to produce actionable market summaries

---

## 2. System Architecture

![System Architecture](docs/system-architecture.png)

### Components:
- **React Frontend:** User interface for searching stocks, viewing macroeconomic data, and managing watchlists.
- **Django REST API:** Backend serving financial and macroeconomic data, plus AI-generated insights.
- **External APIs:**  
  - **Yahoo Finance** — Stock quotes, historical data  
  - **SEC EDGAR** — Company filings and disclosures  
  - **FRED** — Federal Reserve macroeconomic indicators  
  - **Gemini AI** — Natural language summaries and market insights
- **Database:** PostgreSQL or SQLite for persistence.

Data flows from multiple APIs into Django, where it is processed, stored, and exposed to the frontend.

---

## 3. Scope of Work

### Core Features
- Stock quote retrieval and normalization (Yahoo Finance)
- Macroeconomic indicator retrieval (FRED)
- Company filing retrieval (SEC EDGAR)
- AI-powered market summaries (Gemini)
- Watchlist CRUD with persistent storage
- REST API endpoints for frontend integration
- Responsive UI/UX with live updates

### Future Features
- AI-based sentiment analysis of financial news
- Deeper integration with SEC EDGAR filing index
- User authentication and preferences
- Push notifications for market alerts

---

## 4. Kanban Workflow

This project follows **Kanban** for continuous delivery:

| Column | Description |
|--------|-------------|
| Backlog | All planned features and improvements |
| Ready | Groomed tasks ready for development |
| In Progress | Tasks currently being implemented |
| Testing / Review | Awaiting verification and approval |
| Done | Completed and deployed |

---

## 5. Backlog / Future Enhancements
- AI-generated stock & macroeconomic reports
- Automated portfolio performance analysis
- Authentication & user profiles
- Real-time push notifications
- API performance optimization & caching

---

## 6. How to Run Locally

1. Clone the repo  
2. Install backend dependencies:  
   ```bash
   pip install -r requirements.txt
