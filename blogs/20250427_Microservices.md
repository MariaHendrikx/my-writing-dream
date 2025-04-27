# How Microservices Made My Coding Style More Modular (and Scalable)

**TL;DR:**  
Trying microservices forced me to build extremely modular code. Even now, whether I build one app or a full system, I naturally think in small, independent, scalable parts — the way big tech companies like Google probably do.

---

## How Microservices Changed My Coding Forever

Working with microservices completely changed how I think about code.

It **forced** me to be modular.  
Not just slightly modular — *seriously* modular.

When you're building separate services, you have no choice but to think deeply about:
- Clear responsibilities
- Clean boundaries
- Well-defined communication between parts

Otherwise, everything quickly becomes a tangled mess.

At first, I still made mistakes.  
For example, in my `convert-to-epub` microservice, I added authentication logic — even though authentication was already handled by another service.  
That duplication made everything messy and harder to maintain.  
It didn’t take long before I realized I needed to rethink, clean up, and enforce clearer service boundaries.

---

## Modularity Became My Default Coding Style

Since then, **modularity has become my default way of writing code**, even outside of microservices.

Whether I’m working on a small app or a bigger system, I naturally break things into smaller, independent pieces.  
Each piece has one clear purpose.  
Each piece can evolve on its own.

It turns out, this style is incredibly powerful:
- It makes code more **scalable**.
- It makes code more **readable**.
- It makes code **easier to maintain**.
- And when needed, it makes **refactoring much less painful**.

In other words: it’s the foundation for building projects that can actually grow — without collapsing under their own weight.

---

## A Glimpse into Big Tech Architecture

One funny thing I noticed along the way:

Even though I’ve never seen Google’s internal architecture, building modular systems gave me a good intuition about how massive systems like theirs are probably structured.

Thousands of small, independent services.  
Each doing one thing.  
Each replaceable.  
Each able to scale independently.

It’s the only way something at that size could work without falling apart.


## Final Thoughts

I’m still a big fan of microservices, but now I see them differently.  
Microservices aren’t just an architecture — they teach you a **mindset**.

**A mindset of clean boundaries, small responsibilities, and modular design.**  
And you can apply that mindset even if you're building a single monolith app.

Because at any scale — modularity wins.