# AGENTS.md

## Purpose

This project uses **Spec-Driven Development (SDD)** — a workflow where **no code is written until the specification is complete and approved**.

All AI agents (Claude Code, Copilot, Gemini, etc.) must follow the **Spec-Kit lifecycle**:

> **Specify → Plan → Tasks → Implement**

This prevents "vibe coding," ensures alignment across agents, and guarantees that every implementation step maps back to an explicit requirement.

---

## How Agents Must Work

Every agent in this project MUST obey these rules:

1. **Never generate code without a referenced specification**
2. **Never modify architecture without updating specs**
3. **Never propose features without specification approval**
4. **Never change approach without updating constitution**
5. **Every code file must reference its specification**

If an agent cannot find the required spec, it must **stop and request it**, not improvise.

---

## Spec-Kit Workflow (Source of Truth)

### 1. Constitution (WHY — Principles & Constraints)

**File**: `constitution.md`

Defines the project's non-negotiables:
- Architecture values
- Security rules
- Tech stack constraints
- Performance expectations
- Coding patterns

Agents must check this before proposing solutions.

---

### 2. Specify (WHAT — Requirements & Acceptance Criteria)

**Files**: `specs/overview.md`, `specs/features/*.md`, `specs/data-model.md`

Contains:
- User journeys
- Requirements
- Acceptance criteria
- Domain rules
- Business constraints

Agents must not infer missing requirements — they must request clarification or propose specification updates.

---

### 3. Plan (HOW — Architecture & Components)

**File**: Implementation plan (in artifacts)

Includes:
- Component breakdown
- System responsibilities
- High-level sequencing

All architectural output MUST be generated from the Specify files.

---

### 4. Tasks (BREAKDOWN — Atomic Work Units)

**File**: `task.md` (in artifacts)

Each Task must contain:
- Task ID
- Clear description
- Expected outputs
- Links back to Specify + Plan sections

Agents **implement only what these tasks define**.

---

### 5. Implement (CODE — Write Only What Tasks Authorize)

Agents now write code, but must:
- Reference Task IDs
- Follow the Plan exactly
- Not invent new features or flows
- Stop and request clarification if anything is underspecified

> **The golden rule: No task = No code.**

---

## Agent Behavior in This Project

### When generating code:

Agents must reference:
```python
# [Spec]: specs/features/task-crud.md § Add Task
# [Constitution]: constitution.md § Error Handling
# [Task]: T-006
def add_task(title: str, description: str = "") -> Task:
    """Implementation per specification."""
    pass
```

### When proposing architecture:

Agents must reference:
```
Update required in specs/data-model.md → add new field X
```

### When proposing new behavior or features:

Agents must reference:
```
Requires update in specs/features/*.md (WHAT)
```

### When changing principles:

Agents must reference:
```
Modify constitution.md → Principle #X
```

---

## Agent Failure Modes (What Agents MUST Avoid)

Agents are NOT allowed to:

- ❌ Freestyle code or architecture
- ❌ Generate missing requirements
- ❌ Create tasks on their own
- ❌ Alter stack choices without justification
- ❌ Add endpoints, fields, or flows not in the spec
- ❌ Ignore acceptance criteria
- ❌ Produce "creative" implementations that violate the plan

If a conflict arises between spec files, the **Constitution > Specify > Plan > Tasks** hierarchy applies.

---

## Developer–Agent Alignment

Humans and agents collaborate, but the **spec is the single source of truth**.

Before every session, agents should re-read:
1. `constitution.md`
2. `specs/overview.md`
3. Relevant feature specs

This ensures predictable, deterministic development.

---

## Project Structure

```
d:\Hackathon\
├── constitution.md          # WHY (principles)
├── specs/                   # WHAT (requirements)
│   ├── overview.md
│   ├── features/
│   │   └── task-crud.md
│   └── data-model.md
├── src/                     # CODE (implementation)
│   ├── models/
│   ├── storage/
│   ├── services/
│   ├── ui/
│   └── main.py
├── README.md                # User documentation
├── CLAUDE.md                # Claude Code instructions
├── AGENTS.md                # This file
└── pyproject.toml           # UV configuration
```

---

## Spec-Driven Development Workflow

### Step 1: Specify
Write detailed specifications in `/specs` folder.

### Step 2: Plan
Create implementation plan from specifications.

### Step 3: Tasks
Break down plan into atomic, testable tasks.

### Step 4: Implement
Generate code from tasks using AI agents.

### Step 5: Verify
Test against acceptance criteria.

### Step 6: Iterate
Refine specs if needed, regenerate code.

---

## Constitution vs. AGENTS.md

**AGENTS.md (The "How")**: Focuses on interaction. "Use these tools, follow this order, use these patterns."

**constitution.md (The "What")**: Focuses on standards. "We prioritize performance, we use type hints, we require error handling."

---

## Compliance Checklist

Before considering any code complete, verify:

- ✅ Specification exists and is followed
- ✅ Constitution principles adhered to
- ✅ Task ID referenced in code
- ✅ Type hints on all functions
- ✅ Docstrings on all public APIs
- ✅ Error handling implemented
- ✅ Layer separation maintained
- ✅ Manual testing completed
- ✅ Documentation updated

---

## Amendment Process

This file can be updated when:
1. New requirements emerge
2. Better patterns are discovered
3. Phase progression requires changes

**Process**: Update AGENTS.md → Update constitution → Update specs → Regenerate code
