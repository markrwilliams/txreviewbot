import attr
from automat import MethodicalMachine


@attr.s
class AddLabel(object):
    name = attr.ib()


@attr.s
class RemoveLabel(object):
    name = attr.ib()


class ReviewMachine(object):
    _machine = MethodicalMachine()

    @_machine.input()
    def review(self, pullRequest):
        """

        """

    @_machine.input()
    def close(self, pullRequest):
        """

        """

    @_machine.input()
    def approve(self, pullRequest):
        """

        """

    @_machine.input()
    def requestChanges(self, pullRequest):
        """

        """

    @_machine.input()
    def unsubmit(self, pullRequest):
        """

        """

    @_machine.input()
    def merge(self, pullRequest):
        """

        """

    @_machine.state(initial=True)
    def unsubmitted(self):
        """
        A PR that is open but not up for review.
        """

    @_machine.state()
    def closed(self):
        """

        """

    @_machine.state()
    def needsReview(self):
        """

        """

    @_machine.state()
    def approved(self):
        """

        """

    @_machine.state()
    def changesNeeded(self):
        """

        """

    @_machine.state()
    def merged(self):
        """

        """

    @_machine.output()
    def addReviewLabel(self, pullRequest):
        return [AddLabel("review")]

    @_machine.output()
    def removeReviewLabel(self, pullRequest):
        return [RemoveLabel("review")]

    unsubmitted.upon(review, enter=needsReview, outputs=[addReviewLabel])
    unsubmitted.upon(close, enter=closed, outputs=[removeReviewLabel])

    needsReview.upon(approve, enter=approved,
                     outputs=[removeReviewLabel])
    needsReview.upon(requestChanges, enter=changesNeeded,
                     outputs=[removeReviewLabel])
    needsReview.upon(unsubmit, enter=unsubmitted,
                     outputs=[removeReviewLabel])
    needsReview.upon(close, enter=closed,
                     outputs=[removeReviewLabel])

    approved.upon(merge, enter=merged, outputs=[])
    approved.upon(unsubmit, enter=unsubmitted, outputs=[])
    approved.upon(close, enter=closed, outputs=[])

    approved.upon(unsubmit, enter=unsubmitted, outputs=[])
    approved.upon(close, enter=closed, outputs=[])

    closed.upon(unsubmit, enter=unsubmitted, outputs=[])

    changesNeeded.upon(review, enter=needsReview,
                       outputs=[addReviewLabel])
    changesNeeded.upon(unsubmit, enter=unsubmitted,
                       outputs=[])
    changesNeeded.upon(close, enter=closed,
                       outputs=[])
