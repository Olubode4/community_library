#!/bin/bash

# A script that executes the project's tests and then generates a code coverage
# report. Exits with a status of 2 if the code coverage threshold is not
# satisfied.

#cd "$(dirname "$0")"/../locallibrary || exit 1
cd "$(dirname "$0")"/ || exit 1


generate_coverage_html() {
#    coverage html --rcfile='../.coveragerc' --directory='../coverage/'
    coverage html --rcfile='.coveragerc' --directory='../coverage/'
}

handle_report_error() {
    ERROR_STATUS="$1"

    if [ "$ERROR_STATUS" = "2" ]
    then
        echo "ERROR: Failed to meet test coverage threshold"
    else
        echo "ERROR: Unexpected error status while generating code coverage report: $ERROR_STATUS"
    fi

    # Ensure the HTML report is available even though there was an error
    generate_coverage_html

    exit "$ERROR_STATUS"
}

# Ensure that a test failure error propagates to the caller of this script
trap 'exit $?' ERR

rm -rf ../coverage

#coverage run --rcfile='../.coveragerc' --omit=blub manage.py test
#coverage run --rcfile='../.coveragerc' manage.py test -v 2
#coverage run --rcfile='../.coveragerc' manage.py test
coverage run --rcfile='.coveragerc' ../manage.py test


# Handle the error that occurs when the coverage threshold is not met
trap 'handle_report_error $?' ERR

# The --omit flag below is necessary because the jedi package uses `compile`
# to compile some code at runtime and passes the filename "blub" to `compile`.
# This confuses coverage at report time because there is no source file named
# "blub", so we just ignore it here.
#coverage report --rcfile='../.coveragerc'  --omit=blub
#coverage report --rcfile='../.coveragerc'
coverage report --rcfile='.coveragerc'
generate_coverage_html
