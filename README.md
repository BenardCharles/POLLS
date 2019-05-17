# POLLS
Creating a polling app following django tutorials

It’ll consist of two parts:
  - A public site that lets people view polls and vote in them.
  - An admin site that lets you add, change, and delete polls.


In our simple poll app, we’ll create two models: Question and Choice. A Question has a question and a publication date. A Choice has two fields: the text of the choice and a vote tally. Each Choice is associated with a Question.

In our poll application, we’ll have the following four views:

  - Question “index” page – displays the latest few questions.
  - Question “detail” page – displays a question text, with no results but with a form to vote.
  - Question “results” page – displays results for a particular question.
  - Vote action – handles voting for a particular choice in a particular question.