import { useEffect, useState } from "react";

const API = "http://localhost:8000";

type Incident = {
  id: number; title: string; service: string; environment: string; started_at: string; status: string;
};

type Detail = {
  incident: Incident;
  evidence: Array<{id:number; source:string; service:string; timestamp:string; severity:string; message:string}>;
  investigation?: {summary:string; confidence:number; evidence_count:number; hypothesis:string; recommendation:string};
};

export default function App() {
  const [incidents, setIncidents] = useState<Incident[]>([]);
  const [selected, setSelected] = useState<Detail | null>(null);
  const [loading, setLoading] = useState(false);

  async function load() {
    const r = await fetch(`${API}/api/v1/incidents`);
    setIncidents(await r.json());
  }

  async function openIncident(id:number) {
    const r = await fetch(`${API}/api/v1/incidents/${id}`);
    setSelected(await r.json());
  }

  async function investigate(id:number) {
    setLoading(true);
    await fetch(`${API}/api/v1/incidents/${id}/investigate`, {method:"POST"});
    await openIncident(id);
    await load();
    setLoading(false);
  }

  useEffect(() => { load(); }, []);

  return (
    <div className="shell">
      <aside>
        <div className="brand"><span>O</span> OpsPilot AI</div>
        <p className="muted">Evidence-first operations intelligence</p>
        <div className="nav active">Incidents</div>
        <div className="nav">Evidence</div>
        <div className="nav">Audit trail</div>
      </aside>

      <main>
        <header>
          <div>
            <div className="eyebrow">OPERATIONS CONTROL</div>
            <h1>Incident Intelligence</h1>
            <p>Correlate evidence before forming a hypothesis.</p>
          </div>
          <button onClick={load}>Refresh</button>
        </header>

        <section className="stats">
          <div><small>Open incidents</small><strong>{incidents.length}</strong></div>
          <div><small>Evidence model</small><strong>Active</strong></div>
          <div><small>Automation</small><strong>Policy-gated</strong></div>
        </section>

        <div className="grid">
          <section className="panel">
            <div className="panel-title">Incidents</div>
            {incidents.length === 0 ? (
              <div className="empty">No incidents yet. Create one through the API.</div>
            ) : incidents.map(i => (
              <button className="incident" key={i.id} onClick={() => openIncident(i.id)}>
                <div>
                  <strong>{i.title}</strong>
                  <span>{i.service} · {i.environment}</span>
                </div>
                <span className="status">{i.status}</span>
              </button>
            ))}
          </section>

          <section className="panel detail">
            {!selected ? (
              <div className="empty large">Select an incident to inspect its evidence.</div>
            ) : (
              <>
                <div className="detail-head">
                  <div>
                    <div className="eyebrow">INCIDENT #{selected.incident.id}</div>
                    <h2>{selected.incident.title}</h2>
                    <p>{selected.incident.service} · {selected.incident.environment}</p>
                  </div>
                  <button disabled={loading} onClick={() => investigate(selected.incident.id)}>
                    {loading ? "Investigating…" : "Run investigation"}
                  </button>
                </div>

                {selected.investigation && (
                  <div className="analysis">
                    <div className="score">
                      <small>Confidence</small>
                      <strong>{Math.round(selected.investigation.confidence * 100)}%</strong>
                    </div>
                    <div>
                      <small>Summary</small>
                      <p>{selected.investigation.summary}</p>
                      <small>Hypothesis</small>
                      <p>{selected.investigation.hypothesis}</p>
                      <small>Recommendation</small>
                      <p>{selected.investigation.recommendation}</p>
                    </div>
                  </div>
                )}

                <div className="panel-title">Evidence timeline</div>
                <div className="timeline">
                  {selected.evidence.map(e => (
                    <div className="event" key={e.id}>
                      <div className="dot"></div>
                      <div>
                        <div className="event-meta">{e.timestamp} · {e.source} · {e.severity}</div>
                        <strong>{e.message}</strong>
                        <div className="event-service">{e.service}</div>
                      </div>
                    </div>
                  ))}
                </div>
              </>
            )}
          </section>
        </div>
      </main>
    </div>
  );
}
