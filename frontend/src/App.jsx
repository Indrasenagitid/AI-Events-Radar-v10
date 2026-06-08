import { useEffect, useState } from "react";
import { getAIUpdates, getAISummits } from "./api";
import {
  Bell,
  Bot,
  CalendarDays,
  Cpu,
  Database,
  Globe,
  GraduationCap,
  LayoutDashboard,
  Newspaper,
  Search,
  Settings,
  ShieldCheck,
  Sparkles,
  UserCircle,
  Users,
  Zap,
} from "lucide-react";

function App() {
  const [activePage, setActivePage] = useState("CEO Dashboard");

  return (
    <div className="min-h-screen bg-[#070A16] text-white flex">
      <aside className="w-72 bg-white/5 border-r border-white/10 p-6">
        <div className="flex items-center gap-3 mb-8">
          <div className="h-11 w-11 rounded-2xl bg-blue-600 flex items-center justify-center">
            <Sparkles size={24} />
          </div>
          <div>
            <h1 className="text-xl font-bold">AI Events Radar</h1>
            <p className="text-xs text-slate-400">Powered by VKNOWTECH AI</p>
          </div>
        </div>

        <nav className="space-y-3">
          <MenuItem icon={<LayoutDashboard />} label="CEO Dashboard" activePage={activePage} setActivePage={setActivePage} />
          <MenuItem icon={<CalendarDays />} label="AI Events" activePage={activePage} setActivePage={setActivePage} />
          <MenuItem icon={<Users />} label="AI Jobs Radar" activePage={activePage} setActivePage={setActivePage} />
          <MenuItem icon={<Newspaper />} label="AI News Radar" activePage={activePage} setActivePage={setActivePage} />
          <MenuItem icon={<GraduationCap />} label="Learning Hub" activePage={activePage} setActivePage={setActivePage} />
          <MenuItem icon={<Settings />} label="Platform Status" activePage={activePage} setActivePage={setActivePage} />
        </nav>
      </aside>

      <main className="flex-1 overflow-auto">
        <TopBar activePage={activePage} />
        <div className="p-8">
          {activePage === "CEO Dashboard" && <Dashboard />}
          {activePage !== "CEO Dashboard" && <SimplePage title={activePage} />}
        </div>
      </main>
    </div>
  );
}

function Dashboard() {
  const [aiUpdates, setAIUpdates] = useState([]);
  const [summits, setSummits] = useState([]);

  useEffect(() => {
    getAIUpdates()
      .then((data) => setAIUpdates(data.updates || []))
      .catch((error) => console.error("AI Updates API Error:", error));

    getAISummits()
      .then((data) => setSummits(data.summits || []))
      .catch((error) => console.error("AI Summits API Error:", error));
  }, []);

  const globalSummits = summits.filter((item) => item.region === "Global");
  const indiaSummits = summits.filter((item) => item.region === "India");

  return (
    <>
      <Hero />

      <SectionTitle icon="🚀" title="AI Events Intelligence Overview" />

      <div className="grid grid-cols-5 gap-5 mb-8">
        <Kpi title="Total Summits" value={summits.length} icon={<CalendarDays />} />
        <Kpi title="Global Events" value={globalSummits.length} icon={<Globe />} />
        <Kpi title="India Events" value={indiaSummits.length} icon={<Zap />} />
        <Kpi title="Latest AI News" value={aiUpdates.length} icon={<Newspaper />} />
        <Kpi title="Sources" value="Live" icon={<Database />} />
      </div>

      <SectionTitle icon="🌍" title="Top Global AI Summits" />

      <div className="grid grid-cols-2 gap-6 mb-8">
        {globalSummits.map((item) => (
          <SummitCard key={item.registration_url} {...item} />
        ))}
      </div>

      <SectionTitle icon="🇮🇳" title="Top India AI Summits" />

      <div className="grid grid-cols-2 gap-6 mb-8">
        {indiaSummits.map((item) => (
          <SummitCard key={item.registration_url} {...item} />
        ))}
      </div>

      <SectionTitle icon="📰" title="Latest Global AI Updates" />

      <div className="grid grid-cols-2 gap-6 mb-8">
        {aiUpdates.slice(0, 10).map((item) => (
          <AIUpdateCard key={item.link} {...item} />
        ))}
      </div>
    </>
  );
}

function Hero() {
  return (
    <div className="rounded-3xl bg-gradient-to-br from-[#08203D] to-[#0B1020] border border-white/10 p-7 mb-6">
      <p className="text-sm text-yellow-300 mb-3">AI EVENTS RADAR v10</p>
      <h2 className="text-4xl font-bold leading-tight">
        Global AI Events & Technology Intelligence Platform
      </h2>
      <p className="text-yellow-300 font-semibold mt-4">
        Track AI summits, conferences, tech events, news and learning opportunities worldwide.
      </p>
      <p className="text-slate-300 mt-3 max-w-4xl">
        Built for teams and leadership to identify high-value AI events worth attending, registering, learning from, and tracking continuously.
      </p>
    </div>
  );
}

function SummitCard({
  event_name,
  event_date,
  event_location,
  registration_url,
  source_name,
  region,
  category,
  priority,
  status,
}) {
  return (
    <div className="rounded-3xl bg-white/5 border border-white/10 p-6 hover:bg-white/10 transition">
      <div className="flex items-center justify-between mb-3">
        <p className="text-xs text-blue-300">{region}</p>
        <span className="text-xs bg-green-500/20 text-green-300 px-3 py-1 rounded-full">
          {status}
        </span>
      </div>

      <h3 className="text-xl font-bold mb-3">{event_name}</h3>

      <p className="text-sm text-slate-300 mb-2">Category: {category}</p>
      <p className="text-sm text-slate-300 mb-2">Date: {event_date}</p>
      <p className="text-sm text-slate-300 mb-2">Location: {event_location}</p>
      <p className="text-sm text-slate-400 mb-2">Source: {source_name}</p>
      <p className="text-sm text-yellow-300 mb-5">Business Priority: {priority}</p>

      <a
        href={registration_url}
        target="_blank"
        rel="noreferrer"
        className="inline-block rounded-xl bg-blue-600 px-4 py-3 text-sm"
      >
        Open Registration / Event Page
      </a>
    </div>
  );
}

function AIUpdateCard({ title, source, technology, published, link }) {
  return (
    <div className="rounded-3xl bg-white/5 border border-white/10 p-6 hover:bg-white/10 transition">
      <p className="text-xs text-blue-300 mb-2">{source}</p>
      <h3 className="text-lg font-bold mb-4">{title}</h3>
      <p className="text-sm text-slate-300 mb-2">Technology: {technology}</p>
      <p className="text-sm text-slate-400 mb-5">Published: {published}</p>

      <a
        href={link}
        target="_blank"
        rel="noreferrer"
        className="inline-block rounded-xl bg-blue-600 px-4 py-3 text-sm"
      >
        Open Update
      </a>
    </div>
  );
}

function TopBar({ activePage }) {
  return (
    <div className="sticky top-0 z-20 bg-[#070A16]/90 backdrop-blur-xl border-b border-white/10 px-8 py-4 flex items-center justify-between">
      <div>
        <p className="text-xs text-blue-300">AI EVENTS RADAR v10</p>
        <h2 className="text-xl font-bold">{activePage}</h2>
      </div>

      <div className="flex items-center gap-4">
        <div className="flex items-center gap-3 bg-white/5 border border-white/10 rounded-2xl px-4 py-3 w-96">
          <Search size={18} className="text-slate-400" />
          <input className="bg-transparent outline-none text-sm w-full" placeholder="Search AI events..." />
        </div>

        <button className="rounded-2xl bg-blue-600 px-4 py-3 text-sm flex items-center gap-2">
          <Bot size={18} /> AI Agent
        </button>

        <button className="rounded-2xl bg-white/5 border border-white/10 p-3">
          <Bell size={18} />
        </button>

        <div className="flex items-center gap-2 rounded-2xl bg-white/5 border border-white/10 px-4 py-3">
          <UserCircle size={20} />
          <span className="text-sm">Global AI View</span>
        </div>
      </div>
    </div>
  );
}

function SimplePage({ title }) {
  return (
    <>
      <Hero />
      <SectionTitle icon="📌" title={title} />
      <div className="rounded-3xl bg-white/5 border border-white/10 p-6">
        This page will be connected in the next phase.
      </div>
    </>
  );
}

function SectionTitle({ icon, title }) {
  return (
    <div className="mb-4 rounded-2xl bg-white/5 border border-white/10 px-5 py-4">
      <h3 className="text-xl font-bold">{icon} {title}</h3>
    </div>
  );
}

function MenuItem({ icon, label, activePage, setActivePage }) {
  const active = activePage === label;

  return (
    <button
      onClick={() => setActivePage(label)}
      className={`w-full flex items-center gap-3 px-4 py-3 rounded-2xl ${
        active ? "bg-blue-600 text-white" : "text-slate-300 hover:bg-white/10"
      }`}
    >
      <span className="w-5 h-5">{icon}</span>
      <span>{label}</span>
    </button>
  );
}

function Kpi({ title, value, icon }) {
  return (
    <div className="rounded-3xl bg-white/5 border border-white/10 p-5 hover:bg-white/10 transition">
      <div className="flex items-center justify-between mb-4">
        <p className="text-sm text-slate-400">{title}</p>
        <div className="text-blue-300">{icon}</div>
      </div>
      <h3 className="text-3xl font-bold">{value}</h3>
    </div>
  );
}

export default App;