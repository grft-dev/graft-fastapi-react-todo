function CountBadge({ children, primary = false, testId }) {
  return (
    <span
      data-testid={testId}
      style={{
        fontSize: 12,
        fontWeight: 600,
        padding: "4px 10px",
        borderRadius: 20,
        background: primary ? "#eff6ff" : "#f8fafc",
        color: primary ? "#2563eb" : "#64748b",
        border: `1px solid ${primary ? "#dbeafe" : "#e2e8f0"}`,
      }}
    >
      {children}
    </span>
  );
}

function AppHeader({ pendingCount, completedCount }) {
  return (
    <header style={{ borderBottom: "1px solid #e2e8f0", position: "sticky", top: 0, zIndex: 10, background: "#fff" }}>
      <div style={{ maxWidth: 680, margin: "0 auto", padding: "20px 24px", display: "flex", alignItems: "baseline", justifyContent: "space-between" }}>
        <div>
          <h1 style={{ fontFamily: "'Fraunces', Georgia, serif", fontWeight: 400, fontSize: "clamp(26px, 4vw, 34px)", color: "#1e3a8a", margin: 0 }}>
            Todo List App
          </h1>
          <p style={{ margin: "4px 0 0", fontSize: 13, color: "#94a3b8", fontWeight: 500 }}>Keep things moving</p>
        </div>
        <div style={{ display: "flex", gap: 8 }}>
          <CountBadge primary testId="pending-count">{pendingCount} Pending</CountBadge>
          <CountBadge testId="completed-count">{completedCount} Done</CountBadge>
        </div>
      </div>
    </header>
  );
}

export default AppHeader;
