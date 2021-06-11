from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = 'Closes the specified poll for voting'

    def add_arguments(self, parser):
        # parser.add_argument('poll_ids', nargs='+', type=int)
        pass

    def handle(self, *args, **options):
        try:
            print('TODO')
        except Exception:  # nigdy tak nie rób ;-)
            raise CommandError('get_lotto_results failed')
        self.stdout.write(self.style.SUCCESS('Successfully get lotto results'))
