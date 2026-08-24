const pageContainer = [];
pageContainer[0] = smp("Welcome to our exhibition about Asia!",'int-0.png');
pageContainer[1] = smp("we decided we're going to talk about mainly about the Indian subcontinent(and of course india).", 'int-1.png');
pageContainer[2] = simpleContentChapter(`<p><strong>Indian subcontinent</strong> — mainly India itself.</p>
      <img src="./img/IndianSubContinent.jpg" alt="Map of the Indian subcontinent" />`, 0);

pageContainer[3] = simpleContentChapter(`

      <p><strong>Why Europeans came:</strong></p>
      <ul>
        <li>Europeans don't have spices so bland food</li>
        <li>spread christianity</li>
      </ul>
      <img src="./img/0.png" alt="Illustration 0" />
    
  `, 0);


pageContainer[4] = simpleContentChapter(`
      <blockquote>
        “There's a reason why there are too many Asian restaurants all over the world.”
        <cite>(There's a few Europeans restaurant though)</cite>
      </blockquote>
      <img src="./img/1.png" alt="Illustration 1" />
  `, 0);

pageContainer[5] = simpleContentChapter(`
        <p>The ottoman empire controlled Asian trading</p>
      <img src="./img/2.jpg" alt="Ottoman empire on the way of Europe" />
`, 1);
pageContainer[6] = simpleContentChapter(`
      <p>European colonization in India began with the Portuguese.</p>
      <img src="./img/3.jpg" alt="Portuguese colonization illustration" />
 
  `, 1);
