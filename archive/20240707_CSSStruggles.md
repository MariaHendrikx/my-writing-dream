# CSS Struggles

So, yesterday I was trying to finish my portfolio website and I was trying to implement some cool animations. And then it occured to me, that I was actually spending hours on this small animation. I know that when I am coding with Unity, animations are quite easy and quick to implement, but in css... everytime I implement something, be it animations or just centering a div... it can takes hours, because I can't find why the style is not changing. So..today's blog is going to be about CSS and it's struggles.

P.s: If the computer science world should improve something, I think it should be designing an alternative to CSS (that is not based on CSS, such as Vuetify , Bootstrap, or Material UI).

## A List of certain struggles

### 1. **Global Scope**
   - **Struggle:** All CSS rules are applied globally, making it easy to accidentally affect unintended parts of a webpage.
   - **Why It's a struggle:** This can lead to unexpected side effects and makes it challenging to manage large codebases.

### 2. **Specificity and Inheritance**
   - **Struggle:** The specificity rules and inheritance hierarchy can be confusing and difficult to manage.
   - **Why It's a struggle:** Overriding styles can become a complex task, leading to overly specific selectors or the frequent use of `!important`.

### 3. **Box Model Issues**
   - **Struggle:** The box model, especially the differences between `content-box` and `border-box`, can cause layout issues.
   - **Why It's a struggle:** Misunderstanding the box model can lead to unexpected padding, margins, and borders, complicating layout design.

### 4. **Floats and Clearfixes**
   - **Struggle:** Using floats for layout can lead to issues like collapsing parent containers.
   - **Why It's a struggle:** Clearfix hacks are often needed to fix these issues, which can clutter the code and make it harder to maintain.

### 5. **Browser Compatibility**
   - **Struggle:** Different browsers interpret CSS differently, leading to inconsistent styles across platforms.
   - **Why It's a struggle:** Developers need to write additional code to ensure compatibility, increasing development time and complexity.

### 6. **Positioning**
   - **Struggle:** Using `position: relative`, `absolute`, `fixed`, and `sticky` can be tricky, especially in complex layouts.
   - **Why It's a struggle:** Incorrect use can result in elements not appearing where expected, overlapping, or causing layout shifts.

### 7. **Responsive Design**
   - **Struggle:** Creating responsive designs that work across all devices and screen sizes can be challenging.
   - **Why It's a struggle:** Requires a deep understanding of media queries, flexible grids, and sometimes complex calculations to ensure consistency.

### 8. **Lack of Variables (Pre-CSS3)**
   - **Struggle:** Before CSS3, CSS did not support variables, leading to repetitive code and difficulty in maintaining consistent styles.
   - **Why It's a struggle:** Any change required updates across multiple places, increasing the risk of errors and inconsistencies.

### 9. **Complex Animations**
   - **Struggle:** Creating complex animations with CSS can be cumbersome and unintuitive compared to JavaScript-based solutions.
   - **Why It's a struggle:** CSS animations can be limited in functionality and more difficult to debug.

### 10. **Lack of Logical Functions**
   - **Struggle:** CSS lacks logical functions like loops and conditionals, making it harder to create dynamic styles.
   - **Why It's a struggle:** This limitation forces developers to rely on pre-processors like SASS or LESS, adding an additional layer of complexity.

### 11. **Maintenance**
   - **Struggle:** Keeping a large CSS codebase clean and manageable is difficult.
   - **Why It's a struggle:** Without strict naming conventions and organization, the CSS file can become unwieldy and hard to maintain.

## Conclusion

I keep liking it that, if I ask ChatGPT questions, he answers quite good. For me the struggles mentions are indeed the things I am struggling with. In another blog-post I will try to investigate possible solutions.
