"""Generate Moosa_Alam_Resume_2026.pdf — run from repo root."""
from pathlib import Path

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

OUT = Path(__file__).resolve().parents[1] / "public" / "Moosa_Alam_Resume_2026.pdf"

MARGIN = 0.55 * inch


def styles():
    base = getSampleStyleSheet()
    return {
        "name": ParagraphStyle(
            "Name",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=18,
            leading=22,
            spaceAfter=4,
        ),
        "contact": ParagraphStyle(
            "Contact",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.5,
            leading=11,
            textColor="#333333",
            spaceAfter=8,
        ),
        "section": ParagraphStyle(
            "Section",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=13,
            spaceBefore=8,
            spaceAfter=3,
            textColor="#111111",
        ),
        "body": ParagraphStyle(
            "Body",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9,
            leading=12,
            textColor="#222222",
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9,
            leading=11.5,
            leftIndent=10,
            bulletIndent=0,
            textColor="#222222",
            spaceAfter=1.5,
        ),
        "role": ParagraphStyle(
            "Role",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=9.5,
            leading=12,
        ),
        "meta": ParagraphStyle(
            "Meta",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8.5,
            leading=11,
            textColor="#444444",
        ),
    }


def hr():
    return HRFlowable(width="100%", thickness=0.8, color="#222222", spaceBefore=1, spaceAfter=4)


def row(left, right, s):
    return Table(
        [[Paragraph(left, s["role"]), Paragraph(right, s["meta"])]],
        colWidths=[5.2 * inch, 2.0 * inch],
    )


def bullets(items, s):
    return [Paragraph(f"- {item}", s["bullet"]) for item in items]


def build():
    s = styles()
    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=letter,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=0.45 * inch,
        bottomMargin=0.45 * inch,
    )
    story = []

    story.append(Paragraph("Moosa Alam", s["name"]))
    story.append(
        Paragraph(
            "437-212-7641 · malam20@uoguelph.ca · linkedin.com/in/moosa-alam · "
            "github.com/kenjiifx · moosaalam.vercel.app",
            s["contact"],
        )
    )

    story.append(Paragraph("Education", s["section"]))
    story.append(hr())
    story.append(
        row(
            "University of Guelph — Bachelor of Computing, Computer Science (Co-op)",
            "Guelph, ON",
            s,
        )
    )
    story.append(
        Paragraph(
            "Specialization in Cybersecurity · 2025 – 2030",
            s["meta"],
        )
    )
    story.append(Spacer(1, 4))

    story.append(Paragraph("Technical Skills", s["section"]))
    story.append(hr())
    skills = [
        (
            "<b>Languages:</b> TypeScript, Python, C, JavaScript, Java, SQL, Bash"
        ),
        (
            "<b>Systems &amp; Infra:</b> Linux, Docker, GitHub Actions CI/CD, "
            "AWS (EC2, S3, IAM), Terraform, pthreads, BSD sockets"
        ),
        (
            "<b>Security &amp; Observability:</b> IAM policy analysis, SARIF, "
            "Prometheus/Grafana, ELK (Logstash/Kibana), PostgreSQL, FastAPI/Flask, pytest"
        ),
    ]
    for line in skills:
        story.append(Paragraph(line, s["body"]))
        story.append(Spacer(1, 2))

    story.append(Paragraph("Experience", s["section"]))
    story.append(hr())

    story.append(row("Software Engineering Intern — Vibez Music", "Toronto, ON", s))
    story.append(Paragraph("Jan 2026 – Apr 2026", s["meta"]))
    story.extend(
        bullets(
            [
                "Improved internal system throughput by 40%+ by designing and deploying "
                "Python-based backend services and automation tooling to eliminate manual "
                "operational bottlenecks.",
                "Reduced incident triage time by implementing strict request validation, "
                "structured JSON logging, and standardized error handling, improving "
                "observability and debugging efficiency.",
                "Owned backend delivery pipelines by integrating CI/CD workflows and "
                "maintaining reliable service deployments used by cross-functional teams.",
            ],
            s,
        )
    )
    story.append(Spacer(1, 5))

    story.append(row("Freelance Web Developer — Self-Employed", "Remote", s))
    story.append(Paragraph("Jun 2024 – Present", s["meta"]))
    story.extend(
        bullets(
            [
                "Delivered 4+ production-grade web systems end-to-end, handling system "
                "design, performance optimization, and deployment.",
                "Optimized frontend and backend performance to achieve 95-100 Lighthouse "
                "scores through asset tuning, caching strategies, and efficient resource loading.",
            ],
            s,
        )
    )

    story.append(Paragraph("Projects", s["section"]))
    story.append(hr())

    story.append(
        row(
            "Agent Seatbelt | TypeScript, CLI, Policy Engine",
            "Apr 2026 – Present",
            s,
        )
    )
    story.extend(
        bullets(
            [
                "Built a runtime firewall for AI coding agents that intercepts shell, "
                "repo, secret, and production-bound actions before execution.",
                "Implemented deterministic risk classification, approval gating, session "
                "receipts, and hash-chained audit trails for local DevSecOps workflows.",
            ],
            s,
        )
    )
    story.append(Spacer(1, 4))

    story.append(
        row(
            "Permission Guard | TypeScript, AWS IAM, SARIF",
            "Apr 2026",
            s,
        )
    )
    story.extend(
        bullets(
            [
                "Shipped a local-first CLI (npm: @kenjiifx/permissionguard) that scans "
                "AWS IAM policies for overly broad permissions and scores risk.",
                "Generated safer, reviewable remediation candidates and SARIF findings "
                "suitable for CI and code scanning pipelines.",
            ],
            s,
        )
    )
    story.append(Spacer(1, 4))

    story.append(
        row(
            "SSH Honeypot &amp; Threat Analytics | AWS, Docker, ELK, Python, Terraform",
            "Dec 2025 – Jan 2026",
            s,
        )
    )
    story.extend(
        bullets(
            [
                "Deployed a cloud-based SSH honeypot on AWS to capture and analyze "
                "real-world attack traffic in a controlled environment.",
                "Processed and analyzed 5,000+ attack events using Python and the ELK "
                "stack to identify attacker behaviors and command execution trends.",
                "Provisioned infrastructure with Terraform, enforcing least-privilege "
                "IAM policies and secure cloud deployment practices.",
            ],
            s,
        )
    )

    story.append(Paragraph("Certifications", s["section"]))
    story.append(hr())
    story.append(
        Paragraph(
            "<b>AWS Certified Cloud Practitioner</b> — In Progress · Amazon Web Services",
            s["body"],
        )
    )
    story.append(Spacer(1, 2))
    story.append(
        Paragraph(
            "<b>CCNA</b> — In Progress · Cisco",
            s["body"],
        )
    )

    doc.build(story)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()
