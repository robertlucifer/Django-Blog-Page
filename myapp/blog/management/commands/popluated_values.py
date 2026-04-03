from blog.models import Post
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "This is used to populate the values"

    def handle(self, *args, **options):
        titles = [
            "Getting Started with Django", "The Power of the ORM", "Class-Based vs Function Views",
            "Middleware Fundamentals", "Security Best Practices", "REST Framework Integration",
            "Database Migrations 101", "Custom User Models", "Signals and Hooks",
            "Template Inheritance", "Async Django Features", "Testing Your Application",
            "Deployment Strategies", "The Django Admin Panel", "Caching for Performance",
            "Form Validation Logic", "Static & Media Files", "Internationalization (i18n)",
            "Task Queues with Celery", "Optimizing Querysets"
        ]

        content = [
            "A comprehensive guide to setting up your first virtual environment and project structure.",
            "Exploring how Django’s Object-Relational Mapper simplifies complex database queries.",
            "A deep dive into when to use logic-heavy functions versus reusable class structures.",
            "Understanding the request/response cycle and how to inject custom logic globally.",
            "Ensuring your application is protected against SQL injection, XSS, and CSRF attacks.",
            "How to build powerful APIs using Django REST Framework (DRF) for mobile or JS frontends.",
            "Mastering the makemigrations and migrate commands to manage your schema safely.",
            "Why you should always start your project with a custom user model instead of the default.",
            "Implementing decoupled logic using Django’s built-in signal dispatcher for post-save actions.",
            "Utilizing {% extends %} and {% block %} to keep your HTML DRY and maintainable.",
            "Leveraging asynchronous views and middleware to handle high-concurrency tasks.",
            "Writing unit and integration tests using Django’s built-in TestCast suite.",
            "A checklist for moving from a local development server to a production Gunicorn/Nginx setup.",
            "Customizing the administrative interface to make data management easy for non-tech users.",
            "Using Redis or Memcached to speed up database-heavy page loads.",
            "Building robust forms with custom clean methods to ensure data integrity.",
            "Managing CSS, JavaScript, and user-uploaded images in a production environment.",
            "Making your application accessible globally through multi-language support.",
            "Offloading long-running processes like email sending to background workers.",
            "Using select_related and prefetch_related to solve the N+1 query problem."
        ]

        image_urls = [
            "https://picsum.photos/id/40/800/400",
            "https://picsum.photos/id/41/800/400",
            "https://picsum.photos/id/42/800/400",
            "https://picsum.photos/id/43/800/400",
            "https://picsum.photos/id/44/800/400",
            "https://picsum.photos/id/45/800/400",
            "https://picsum.photos/id/46/800/400",
            "https://picsum.photos/id/47/800/400",
            "https://picsum.photos/id/48/800/400",
            "https://picsum.photos/id/49/800/400",
            "https://picsum.photos/id/50/800/400",
            "https://picsum.photos/id/51/800/400",
            "https://picsum.photos/id/52/800/400",
            "https://picsum.photos/id/53/800/400",
            "https://picsum.photos/id/54/800/400",
            "https://picsum.photos/id/55/800/400",
            "https://picsum.photos/id/56/800/400",
            "https://picsum.photos/id/57/800/400",
            "https://picsum.photos/id/58/800/400",
            "https://picsum.photos/id/59/800/400",
            "https://picsum.photos/id/60/800/400"
        ]

        for title,content,image_url in zip(titles,content,image_urls):
            Post.objects.create(title=title,content=content,image_url=image_url)
        self.stdout.write(self.style.SUCCESS("Completed inserting"))