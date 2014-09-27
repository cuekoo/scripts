# Git Commands

## discarding

* to discard changes to a staged file

        $ git checkout -- filename

    `--` is used to discriminate it from a `branch`

## gitignore

Refer to this [site](http://git-scm.com/docs/gitignore) for details.

* ignore all files end with `.dSYM`

        *.dSYM

* ignore all files except for `*.foo` [seems to be not working as expected, 
non-empty sub directories are included]

        # Ignore everything
        *
        # Don't ignore directories, so we can recurse into them
        !*/
        # Don't ignore .gitignore and *.foo files
        !.gitignore
        !*.foo

This is the [reference](http://stackoverflow.com/questions/8024924/gitignore-ignore-all-files-then-recursively-allow-foo)


